# -*- encoding: utf-8 -*-
"""
vLEI.app.well_known module

Well-Known KERI OOBI endpoint handler compliant with RFC 8615.

This module implements a well-known endpoint handler that serves KERI resources
based on the identifier type:
- Witnesses (B prefix): HTTP 301 redirect to witness OOBI URL
- Schemas (E prefix in schemas): Schema CESR stream in body
- AIDs (E prefix in aids): KEL CESR stream in body

The handler uses an index.json file to determine the identifier type and
locate the appropriate resource files.

Reference: https://github.com/GLEIF-IT/GLEIF-IT.github.io/tree/main/.well-known
"""
import json
import os
from pathlib import Path
from typing import Optional

import falcon
from keri import help

logger = help.ogler.getLogger()


class WellKnownIndex:
    """
    Manages the well-known index.json and provides lookup functionality.
    
    The index.json structure follows the GLEIF specification:
    {
        "$schema": "...",
        "aids": { "Human Name": "AID_PREFIX", ... },
        "witnesses": { "WIT_PREFIX": "WIT_PREFIX", ... },
        "schemas": { "Schema Name": "SCHEMA_SAID", ... }
    }
    """
    
    def __init__(self, index_path: str):
        """
        Initialize the well-known index from an index.json file.
        
        Parameters:
            index_path (str): Path to the index.json file
        """
        self.index_path = index_path
        self.aids: dict[str, str] = {}
        self.witnesses: dict[str, str] = {}
        self.schemas: dict[str, str] = {}
        self._aid_lookup: set[str] = set()
        self._witness_lookup: set[str] = set()
        self._schema_lookup: set[str] = set()
        
        self._load_index()
    
    def _load_index(self):
        """Load and parse the index.json file."""
        if not os.path.exists(self.index_path):
            logger.warning(f"Well-known index not found at {self.index_path}")
            return
            
        try:
            with open(self.index_path, 'r') as f:
                data = json.load(f)
                
            self.aids = data.get("aids", {})
            self.witnesses = data.get("witnesses", {})
            self.schemas = data.get("schemas", {})
            
            # Build reverse lookup sets for efficient identifier matching
            self._aid_lookup = set(self.aids.values())
            self._witness_lookup = set(self.witnesses.values())
            self._schema_lookup = set(self.schemas.values())
            
            logger.info(f"Loaded well-known index: {len(self.aids)} AIDs, "
                       f"{len(self.witnesses)} witnesses, {len(self.schemas)} schemas")
                       
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse well-known index: {e}")
        except Exception as e:
            logger.error(f"Failed to load well-known index: {e}")
    
    def is_witness(self, identifier: str) -> bool:
        """Check if identifier is a witness (typically B prefix)."""
        return identifier in self._witness_lookup
    
    def is_schema(self, identifier: str) -> bool:
        """Check if identifier is a schema SAID."""
        return identifier in self._schema_lookup
    
    def is_aid(self, identifier: str) -> bool:
        """Check if identifier is an AID."""
        return identifier in self._aid_lookup
    
    def get_type(self, identifier: str) -> Optional[str]:
        """
        Determine the type of identifier.
        
        Returns:
            'witness', 'schema', 'aid', or None if not found
        """
        if self.is_witness(identifier):
            return 'witness'
        if self.is_schema(identifier):
            return 'schema'
        if self.is_aid(identifier):
            return 'aid'
        return None


class WellKnownEnd:
    """
    RFC 8615 compliant well-known KERI OOBI endpoint handler.
    
    Serves KERI resources from /.well-known/keri/oobi/{identifier} based on
    the identifier type:
    
    - Witnesses: KERI rpy message with complete witness set (application/json+cesr)
    - Schemas: Schema CESR stream in response body (application/cesr)
    - AIDs: KEL CESR stream in response body (application/cesr)
    
    Directory structure expected:
        {oobi_dir}/
        ├── index.json          # Index of all identifiers
        └── {identifier}/       # Per-identifier directories
            └── index.json      # KERI rpy message or CESR content
    """
    
    CONTENT_TYPE_CESR = "application/cesr"
    CONTENT_TYPE_JSON_CESR = "application/json+cesr"
    
    def __init__(self, oobi_dir: str):
        """
        Initialize the well-known endpoint handler.
        
        Parameters:
            oobi_dir (str): Path to the well-known/keri/oobi directory
        """
        if "keri/oobi" not in oobi_dir:
            oobi_dir = os.path.join(oobi_dir, "keri", "oobi")
        self.oobi_dir = oobi_dir
        self.index = WellKnownIndex(os.path.join(oobi_dir, "index.json"))
        
        logger.info(f"WellKnownEnd initialized with directory: {oobi_dir}")
    
    def on_get(self, req, rep, identifier: str):
        """
        Handle GET requests for well-known KERI resources.
        Assumes the "keri/oobi" path segment is already included in the self.oobi_dir.
        
        Parameters:
            req (Request): Falcon HTTP Request object
            rep (Response): Falcon HTTP Response object  
            identifier (str): KERI identifier (AID, witness ID, or schema SAID)
        """
        # Determine identifier type from index
        id_type = self.index.get_type(identifier)
        
        if id_type is None:
            # Identifier not found in index - check if directory exists anyway
            id_dir = Path(self.oobi_dir, identifier)
            if not id_dir.exists():
                raise falcon.HTTPNotFound(
                    title="Unknown Identifier",
                    description=f"Identifier {identifier} not found in well-known index"
                )
            # If directory exists but not in index, try to serve as generic CESR
            id_type = self._infer_type_from_prefix(identifier)
        
        # Get the resource file path
        resource_path = Path(self.oobi_dir, identifier, "index.json")
        if not resource_path.exists():
            raise falcon.HTTPNotFound(
                title="Resource Not Found",
                description=f"Resource file not found for identifier {identifier}"
            )
        
        # Handle based on type
        if id_type == 'witness':
            self._handle_witness(req, rep, identifier, resource_path)
        elif id_type == 'schema':
            self._handle_schema(req, rep, identifier, resource_path)
        elif id_type == 'aid':
            self._handle_aid(req, rep, identifier, resource_path)
        else:
            # Unknown type - serve raw content
            self._handle_generic(req, rep, identifier, resource_path)
    
    def _infer_type_from_prefix(self, identifier: str) -> str:
        """
        Infer identifier type from CESR prefix when not in index.
        
        CESR prefixes:
        - B: Non-transferable identifier (typically witnesses)
        - E: Transferable identifier or SAID (AIDs, schemas)
        """
        if identifier.startswith('B'):
            return 'witness'
        elif identifier.startswith('E'):
            # Could be AID or schema - default to AID
            return 'aid'
        return 'unknown'
    
    def _handle_witness(self, req, rep, identifier: str, resource_path: Path):
        """
        Handle witness identifier - return rpy message with witness URLs.
        
        The witness resource file contains a KERI rpy message with the complete
        witness set for an AID. We return the entire rpy message so the caller
        can discover all witnesses, not just the first one.
        
        Returns HTTP 200 with the rpy message in the body.
        """
        try:
            with open(resource_path, 'r') as f:
                content = f.read().strip()
            
            # Try to parse as JSON to validate it's a proper rpy message
            try:
                rpy_data = json.loads(content)
                # Return the rpy message as JSON+CESR
                rep.status = falcon.HTTP_200
                rep.content_type = self.CONTENT_TYPE_JSON_CESR
                rep.text = content
            except json.JSONDecodeError:
                # Not JSON - might be raw CESR, serve as-is
                with open(resource_path, 'rb') as f:
                    rep.status = falcon.HTTP_200
                    rep.content_type = self.CONTENT_TYPE_CESR
                    rep.data = f.read()
            
        except Exception as e:
            logger.error(f"Error handling witness {identifier}: {e}")
            raise falcon.HTTPInternalServerError(
                title="Error",
                description=f"Failed to process witness resource: {e}"
            )
    
    def _handle_schema(self, req, rep, identifier: str, resource_path: Path):
        """
        Handle schema identifier - return schema CESR stream in body.
        
        Content-Type: application/cesr
        """
        try:
            with open(resource_path, 'rb') as f:
                content = f.read()
            
            rep.status = falcon.HTTP_200
            rep.content_type = self.CONTENT_TYPE_CESR
            rep.data = content
            
        except Exception as e:
            logger.error(f"Error handling schema {identifier}: {e}")
            raise falcon.HTTPInternalServerError(
                title="Error",
                description=f"Failed to process schema resource: {e}"
            )
    
    def _handle_aid(self, req, rep, identifier: str, resource_path: Path):
        """
        Handle AID identifier - return KEL CESR stream in body.
        
        Content-Type: application/cesr
        """
        try:
            with open(resource_path, 'rb') as f:
                content = f.read()
            
            rep.status = falcon.HTTP_200
            rep.content_type = self.CONTENT_TYPE_CESR
            rep.data = content
            
        except Exception as e:
            logger.error(f"Error handling AID {identifier}: {e}")
            raise falcon.HTTPInternalServerError(
                title="Error",
                description=f"Failed to process AID resource: {e}"
            )
    
    def _handle_generic(self, req, rep, identifier: str, resource_path: Path):
        """
        Handle unknown identifier type - serve raw content as CESR.
        """
        try:
            with open(resource_path, 'rb') as f:
                content = f.read()
            
            rep.status = falcon.HTTP_200
            rep.content_type = self.CONTENT_TYPE_CESR
            rep.data = content
            
        except Exception as e:
            logger.error(f"Error handling generic identifier {identifier}: {e}")
            raise falcon.HTTPInternalServerError(
                title="Error",
                description=f"Failed to process resource: {e}"
            )


def loadWellKnownEnds(app, oobi_dir: str, prefix: str = ""):
    """
    Load well-known KERI OOBI endpoints into a Falcon app.
    
    Parameters:
        app: Falcon application instance
        oobi_dir (str): Path to the well-known/keri/oobi directory
        prefix (str): Optional URL prefix
        
    Returns:
        WellKnownEnd: The endpoint instance for testing/inspection
    """
    well_known_end = WellKnownEnd(oobi_dir)
    app.add_route(prefix + "/.well-known/keri/oobi/{identifier}", well_known_end)
    
    logger.info(f"Loaded well-known endpoint at {prefix}/.well-known/keri/oobi/{{identifier}}")
    
    return well_known_end
