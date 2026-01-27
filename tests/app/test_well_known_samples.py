# -*- encoding: utf-8 -*-
"""
Integration tests for well_known module using the samples/oobis directory.

Tests that the WellKnownEnd handler correctly serves the GLEIF-style
well-known structure from samples/oobis/.well-known/
"""
import json
import os
from pathlib import Path

import falcon
import falcon.testing
import pytest

from vlei.app.well_known import WellKnownEnd, WellKnownIndex, loadWellKnownEnds


@pytest.fixture
def samples_oobi_dir():
    """Get the path to the samples/oobis/.well-known/keri/oobi directory."""
    # Get the vLEI project root (3 levels up from tests/app/)
    test_dir = Path(__file__).parent
    project_root = test_dir.parent.parent
    oobi_dir = project_root / "samples" / "oobis" / ".well-known" / "keri" / "oobi"
    
    if not oobi_dir.exists():
        pytest.skip(f"Samples directory not found at {oobi_dir}")
    
    return str(oobi_dir)


@pytest.fixture
def samples_client(samples_oobi_dir):
    """Create a Falcon test client with the samples well-known endpoint."""
    app = falcon.App()
    loadWellKnownEnds(app, samples_oobi_dir)
    return falcon.testing.TestClient(app)


class TestSamplesWellKnownIndex:
    """Test WellKnownIndex with the samples directory."""
    
    def test_load_gleif_index(self, samples_oobi_dir):
        """Test loading the GLEIF-style index.json."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        # Verify GLEIF AIDs are loaded
        assert "GLEIF RoOT" in index.aids
        assert "GLEIF External" in index.aids
        assert "GLEIF Internal" in index.aids
        
        # Verify witness identifiers
        assert "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS" in index.witnesses
        
        # Verify schema SAIDs
        assert "LegalEntityvLEICredential" in index.schemas
        assert "QualifiedvLEIIssuervLEICredential" in index.schemas
    
    def test_gleif_root_is_aid(self, samples_oobi_dir):
        """Test that GLEIF Root is identified as an AID."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        gleif_root = "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"
        assert index.is_aid(gleif_root) is True
        assert index.get_type(gleif_root) == "aid"
    
    def test_witness_identification(self, samples_oobi_dir):
        """Test witness identifier detection."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        witness_id = "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS"
        assert index.is_witness(witness_id) is True
        assert index.get_type(witness_id) == "witness"
    
    def test_schema_identification(self, samples_oobi_dir):
        """Test schema SAID detection."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        index = WellKnownIndex(index_path)
        
        schema_said = "ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY"
        assert index.is_schema(schema_said) is True
        assert index.get_type(schema_said) == "schema"


class TestSamplesWellKnownEnd:
    """Test WellKnownEnd HTTP handler with samples directory."""
    
    def test_gleif_root_aid_response(self, samples_client):
        """Test fetching GLEIF Root AID returns rpy message with witness URLs."""
        aid_id = "EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2"
        response = samples_client.simulate_get(f"/.well-known/keri/oobi/{aid_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        
        # Verify it contains KERI rpy message
        content = response.text
        assert "rpy" in content
        assert "witness" in content
        assert aid_id in content
    
    def test_gleif_external_aid_response(self, samples_client):
        """Test fetching GLEIF External AID."""
        aid_id = "EINmHd5g7iV-UldkkkKyBIH052bIyxZNBn9pq-zNrYoS"
        response = samples_client.simulate_get(f"/.well-known/keri/oobi/{aid_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        assert aid_id in response.text
    
    def test_witness_response(self, samples_client):
        """Test fetching witness returns KEL with icp and rpy messages."""
        witness_id = "BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS"
        response = samples_client.simulate_get(f"/.well-known/keri/oobi/{witness_id}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        
        # Verify witness KEL content
        content = response.text
        assert "icp" in content  # Inception event
        assert witness_id in content
    
    def test_legal_entity_schema_response(self, samples_client):
        """Test fetching Legal Entity vLEI Credential schema."""
        schema_said = "ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY"
        response = samples_client.simulate_get(f"/.well-known/keri/oobi/{schema_said}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        
        # Parse as JSON schema
        schema = json.loads(response.text)
        assert schema["$id"] == schema_said
        assert schema["credentialType"] == "LegalEntityvLEICredential"
        assert schema["title"] == "Legal Entity vLEI Credential"
    
    def test_qvi_schema_response(self, samples_client):
        """Test fetching QVI vLEI Credential schema."""
        schema_said = "EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao"
        response = samples_client.simulate_get(f"/.well-known/keri/oobi/{schema_said}")
        
        assert response.status == falcon.HTTP_200
        assert response.content_type == "application/cesr"
        
        # Parse as JSON schema
        schema = json.loads(response.text)
        assert schema["$id"] == schema_said
        assert schema["credentialType"] == "QualifiedvLEIIssuervLEICredential"


class TestSamplesStructureCompliance:
    """Test that samples directory complies with GLEIF specification."""
    
    def test_index_has_required_fields(self, samples_oobi_dir):
        """Test that index.json has all required fields per spec."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        
        with open(index_path, 'r') as f:
            index = json.load(f)
        
        # Required fields per GLEIF OOBI schema
        assert "aids" in index
        assert "witnesses" in index
        assert "schemas" in index
        
        # Verify structure
        assert isinstance(index["aids"], dict)
        assert isinstance(index["witnesses"], dict)
        assert isinstance(index["schemas"], dict)
    
    def test_identifier_directories_exist(self, samples_oobi_dir):
        """Test that all identifiers in index have corresponding directories."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        
        with open(index_path, 'r') as f:
            index = json.load(f)
        
        # Check AIDs
        for name, aid in index["aids"].items():
            aid_dir = Path(samples_oobi_dir, aid)
            assert aid_dir.exists(), f"AID directory missing for {name}: {aid}"
            assert (aid_dir / "index.json").exists(), f"index.json missing for {name}"
        
        # Check at least one witness (we don't need all 10)
        witness_ids = list(index["witnesses"].keys())
        if witness_ids:
            witness_id = witness_ids[0]
            witness_dir = Path(samples_oobi_dir, witness_id)
            assert witness_dir.exists(), f"Witness directory missing: {witness_id}"
    
    def test_cesr_identifier_format(self, samples_oobi_dir):
        """Test that identifiers follow CESR format (44 chars, proper prefix)."""
        index_path = os.path.join(samples_oobi_dir, "index.json")
        
        with open(index_path, 'r') as f:
            index = json.load(f)
        
        # Check AIDs (E prefix, 44 chars)
        for name, aid in index["aids"].items():
            assert len(aid) == 44, f"AID {name} wrong length: {len(aid)}"
            assert aid[0] == 'E', f"AID {name} wrong prefix: {aid[0]}"
        
        # Check witnesses (B prefix, 44 chars)
        for witness_id in index["witnesses"].keys():
            assert len(witness_id) == 44, f"Witness wrong length: {len(witness_id)}"
            assert witness_id[0] == 'B', f"Witness wrong prefix: {witness_id[0]}"
        
        # Check schemas (E prefix, 44 chars)
        for schema_name, schema_said in index["schemas"].items():
            assert len(schema_said) == 44, f"Schema {schema_name} wrong length: {len(schema_said)}"
            assert schema_said[0] == 'E', f"Schema {schema_name} wrong prefix: {schema_said[0]}"
