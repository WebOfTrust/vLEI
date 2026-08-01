# -*- encoding: utf-8 -*-
"""
Tests for the well_known module.

Tests the WellKnownEnd handler and WellKnownIndex lookup functionality.
"""
import json
import os
import tempfile
import shutil
from pathlib import Path

import falcon
import falcon.testing
import pytest

from vlei.app.well_known import WellKnownEnd, WellKnownIndex, loadWellKnownEnds


# Test data - simulating GLEIF-style well-known structure
SAMPLE_INDEX = {
    "$schema": "https://example.org/.well-known/keri/oobi/schema.json",
    "aids": {
        "Test Root": "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2",
        "Test External": "EINmHd5g7iV-UldkkkKyBIH052bIyxZNBn9pq-zNrYoS",
    },
    "witnesses": {
        "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS": "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS",
        "BDwydI_FJJ-tvAtCl1tIu_VQqYTI3Q0JyHDhO1v2hZBt": "BDwydI_FJJ-tvAtCl1tIu_VQqYTI3Q0JyHDhO1v2hZBt",
    },
    "schemas": {
        "LegalEntityvLEICredential": "ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY",
        "QualifiedvLEIIssuervLEICredential": "EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao",
    }
}

# Sample witness rpy message with URLs
SAMPLE_WITNESS_RPY = {
    "v": "KERI10JSON000282_",
    "t": "rpy",
    "d": "EPflJSbTCs2WKoGx4zIJ5OpOXHXuY0JE9et9ile2gMpv",
    "dt": "2022-11-21T21:20:24.003241+00:00",
    "r": "/oobi/witness",
    "a": {
        "urls": [
            "http://witness1.example.com:5623/oobi/EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2/witness",
            "http://witness2.example.com:5623/oobi/EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2/witness",
        ],
        "aid": "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS"
    }
}

# Sample KEL content (simplified for testing)
SAMPLE_KEL_CESR = b'{"v":"KERI10JSON000159_","t":"icp","d":"EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"}'

# Sample schema CESR content
SAMPLE_SCHEMA_CESR = b'{"$id":"ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY","$schema":"http://json-schema.org/draft-07/schema#"}'


@pytest.fixture
def well_known_dir():
    """Create a temporary well-known directory structure for testing."""
    tmpdir = tempfile.mkdtemp()
    oobi_dir = os.path.join(tmpdir, ".well-known", "keri", "oobi")
    os.makedirs(oobi_dir)
    
    # Write index.json
    with open(os.path.join(oobi_dir, "index.json"), 'w') as f:
        json.dump(SAMPLE_INDEX, f)
    
    # Create witness directory with rpy message
    witness_id = "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS"
    witness_dir = os.path.join(oobi_dir, witness_id)
    os.makedirs(witness_dir)
    with open(os.path.join(witness_dir, "index.json"), 'w') as f:
        json.dump(SAMPLE_WITNESS_RPY, f)
    
    # Create AID directory with KEL
    aid_id = "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"
    aid_dir = os.path.join(oobi_dir, aid_id)
    os.makedirs(aid_dir)
    with open(os.path.join(aid_dir, "index.json"), 'wb') as f:
        f.write(SAMPLE_KEL_CESR)
    
    # Create schema directory with schema CESR
    schema_id = "ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY"
    schema_dir = os.path.join(oobi_dir, schema_id)
    os.makedirs(schema_dir)
    with open(os.path.join(schema_dir, "index.json"), 'wb') as f:
        f.write(SAMPLE_SCHEMA_CESR)
    
    yield oobi_dir
    
    # Cleanup
    shutil.rmtree(tmpdir)


@pytest.fixture
def client(well_known_dir):
    """Create a Falcon test client with the well-known endpoint."""
    app = falcon.App()
    loadWellKnownEnds(app, well_known_dir)
    return falcon.testing.TestClient(app)


class TestWellKnownIndex:
    """Tests for WellKnownIndex class."""
    
    def test_load_index(self, well_known_dir):
        """Test loading index.json file."""
        index_path = os.path.join(well_known_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        assert len(index.aids) == 2
        assert len(index.witnesses) == 2
        assert len(index.schemas) == 2
    
    def test_is_witness(self, well_known_dir):
        """Test witness identification."""
        index_path = os.path.join(well_known_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        assert index.is_witness("BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS") is True
        assert index.is_witness("BDwydI_FJJ-tvAtCl1tIu_VQqYTI3Q0JyHDhO1v2hZBt") is True
        assert index.is_witness("EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2") is False
    
    def test_is_schema(self, well_known_dir):
        """Test schema identification."""
        index_path = os.path.join(well_known_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        assert index.is_schema("ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY") is True
        assert index.is_schema("EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao") is True
        assert index.is_schema("BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS") is False
    
    def test_is_aid(self, well_known_dir):
        """Test AID identification."""
        index_path = os.path.join(well_known_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        assert index.is_aid("EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2") is True
        assert index.is_aid("EINmHd5g7iV-UldkkkKyBIH052bIyxZNBn9pq-zNrYoS") is True
        assert index.is_aid("BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS") is False
    
    def test_get_type(self, well_known_dir):
        """Test identifier type resolution."""
        index_path = os.path.join(well_known_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        assert index.get_type("BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS") == "witness"
        assert index.get_type("ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY") == "schema"
        assert index.get_type("EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2") == "aid"
        assert index.get_type("unknown_identifier") is None
    
    def test_missing_index_file(self):
        """Test handling of missing index.json."""
        index = WellKnownIndex("/nonexistent/path/index.json")
        
        assert len(index.aids) == 0
        assert len(index.witnesses) == 0
        assert len(index.schemas) == 0


class TestWellKnownEnd:
    """Tests for WellKnownEnd HTTP handler."""
    
    def test_witness_rpy_response(self, client):
        """Test that witness requests return rpy message with witness URLs."""
        witness_id = "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS"
        response = client.simulate_get(f"/.well-known/keri/oobi/{witness_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/json+cesr"
        
        # Parse the rpy message
        rpy_data = json.loads(response.text)
        assert rpy_data["t"] == "rpy"
        assert "urls" in rpy_data["a"]
        assert len(rpy_data["a"]["urls"]) == 2  # Both witness URLs present
        assert "witness1.example.com" in rpy_data["a"]["urls"][0]
        assert "witness2.example.com" in rpy_data["a"]["urls"][1]
    
    def test_schema_cesr_response(self, client):
        """Test that schema requests return CESR in body."""
        schema_id = "ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY"
        response = client.simulate_get(f"/.well-known/keri/oobi/{schema_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        assert b"$schema" in response.content
    
    def test_aid_cesr_response(self, client):
        """Test that AID requests return KEL CESR in body."""
        aid_id = "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"
        response = client.simulate_get(f"/.well-known/keri/oobi/{aid_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        assert b"icp" in response.content  # Inception event marker
    
    def test_unknown_identifier_404(self, client):
        """Test that unknown identifiers return 404."""
        response = client.simulate_get("/.well-known/keri/oobi/unknown_identifier")
        
        assert response.status == falcon.HTTP_404
    
    def test_identifier_not_in_index_but_dir_exists(self, well_known_dir):
        """Test handling of identifier with directory but not in index."""
        # Create a directory for an identifier not in the index
        unknown_id = "EUnknownIdentifier_NotInIndex_ButHasDirectory"
        unknown_dir = os.path.join(well_known_dir, unknown_id)
        os.makedirs(unknown_dir)
        with open(os.path.join(unknown_dir, "index.json"), 'wb') as f:
            f.write(b'{"test": "data"}')
        
        # Create client with updated directory
        app = falcon.App()
        loadWellKnownEnds(app, well_known_dir)
        client = falcon.testing.TestClient(app)
        
        # Should serve the content even if not in index (infers type from prefix)
        response = client.simulate_get(f"/.well-known/keri/oobi/{unknown_id}")
        
        # E prefix infers as AID, returns CESR
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"


class TestWellKnownEndEdgeCases:
    """Edge case tests for WellKnownEnd."""
    
    def test_witness_no_urls_in_rpy(self, well_known_dir):
        """Test witness with empty URLs in rpy message still returns rpy message."""
        # Create witness with no URLs
        witness_id = "BNoUrlsWitness_TestIdentifier_ForEmptyUrls"
        witness_dir = os.path.join(well_known_dir, witness_id)
        os.makedirs(witness_dir)
        
        empty_rpy = {"v": "KERI10JSON", "t": "rpy", "a": {"urls": [], "aid": witness_id}}
        with open(os.path.join(witness_dir, "index.json"), 'w') as f:
            json.dump(empty_rpy, f)
        
        # Add to index
        index_path = os.path.join(well_known_dir, "index.json")
        with open(index_path, 'r') as f:
            index_data = json.load(f)
        index_data["witnesses"][witness_id] = witness_id
        with open(index_path, 'w') as f:
            json.dump(index_data, f)
        
        # Create fresh client
        app = falcon.App()
        loadWellKnownEnds(app, well_known_dir)
        client = falcon.testing.TestClient(app)
        
        response = client.simulate_get(f"/.well-known/keri/oobi/{witness_id}")
        
        # Should return the rpy message as JSON+CESR with empty URLs array
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/json+cesr"
        
        rpy_data = json.loads(response.text)
        assert rpy_data["a"]["urls"] == []
    
    def test_resource_file_missing(self, well_known_dir):
        """Test handling when identifier directory exists but index.json is missing."""
        # Create directory without index.json
        orphan_id = "EOrphanDirectory_NoIndexJson_ShouldFail"
        orphan_dir = os.path.join(well_known_dir, orphan_id)
        os.makedirs(orphan_dir)
        
        # Add to index but don't create the file
        index_path = os.path.join(well_known_dir, "index.json")
        with open(index_path, 'r') as f:
            index_data = json.load(f)
        index_data["aids"]["Orphan"] = orphan_id
        with open(index_path, 'w') as f:
            json.dump(index_data, f)
        
        app = falcon.App()
        loadWellKnownEnds(app, well_known_dir)
        client = falcon.testing.TestClient(app)
        
        response = client.simulate_get(f"/.well-known/keri/oobi/{orphan_id}")
        
        assert response.status == falcon.HTTP_404


class TestLoadWellKnownEnds:
    """Tests for the loadWellKnownEnds helper function."""
    
    def test_load_returns_endpoint(self, well_known_dir):
        """Test that loadWellKnownEnds returns the endpoint instance."""
        app = falcon.App()
        endpoint = loadWellKnownEnds(app, well_known_dir)
        
        assert isinstance(endpoint, WellKnownEnd)
        assert endpoint.oobi_dir == well_known_dir
    
    def test_load_with_prefix(self, well_known_dir):
        """Test loading with URL prefix."""
        app = falcon.App()
        endpoint = loadWellKnownEnds(app, well_known_dir, prefix="/api/v1")
        client = falcon.testing.TestClient(app)
        
        # Should work with prefix
        aid_id = "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"
        response = client.simulate_get(f"/api/v1/.well-known/keri/oobi/{aid_id}")
        
        assert response.status == falcon.HTTP_200
