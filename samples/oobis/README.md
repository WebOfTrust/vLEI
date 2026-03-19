# vLEI Well-Known OOBI Samples

This directory contains sample KERI well-known OOBI resources following the [GLEIF Well-Known URI Structure Specification](https://github.com/GLEIF-IT/GLEIF-IT.github.io/blob/main/.well-known/STRUCTURE.md) and [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615.html).

## Directory Structure

```
.well-known/
├── index.json                  # Main discovery index
├── schema.json                 # JSON Schema for index.json validation
└── keri/
    └── oobi/
        ├── index.json          # OOBI catalog (AIDs, witnesses, schemas)
        ├── schema.json         # JSON Schema for OOBI index validation
        ├── {aid}/              # AID directories (E prefix)
        │   └── index.json      # KERI rpy message with witness URLs
        ├── {witness}/          # Witness directories (B prefix)
        │   └── index.json      # Witness KEL (icp + rpy messages)
        └── {schema}/           # Schema directories (E prefix)
            └── index.json      # ACDC JSON Schema
```

## Resource Types

### AIDs (Autonomic Identifiers)
- **Prefix**: `E` (transferable)
- **Example**: `EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2`
- **Content**: KERI `rpy` message containing witness OOBI URLs
- **Content-Type**: `application/json+cesr` or `application/cesr`

### Witnesses
- **Prefix**: `B` (non-transferable)
- **Example**: `BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS`
- **Content**: Witness KEL (inception event + location scheme + endpoint role)
- **Content-Type**: `application/cesr`

### Schemas
- **Prefix**: `E` (SAID)
- **Example**: `ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY`
- **Content**: ACDC JSON Schema
- **Content-Type**: `application/cesr` or `application/schema+json`

## Discovery Protocol

### 1. Discover Main Index
```bash
curl https://example.org/.well-known/index.json
```

Returns metadata and references to AIDs, witnesses, and schemas.

### 2. Discover OOBI Catalog
```bash
curl https://example.org/.well-known/keri/oobi/index.json
```

Returns flat map of all identifiers by type.

### 3. Resolve Specific Resource
```bash
# Get GLEIF Root AID witness URLs
curl https://example.org/.well-known/keri/oobi/EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2/index.json

# Get witness KEL
curl https://example.org/.well-known/keri/oobi/BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS/index.json

# Get schema
curl https://example.org/.well-known/keri/oobi/ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY/index.json
```

## Sample Resources Included

### AIDs (3 total)
- **GLEIF RoOT**: `EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2`
- **GLEIF External**: `EINmHd5g7iV-UldkkkKyBIH052bIyxZNBn9pq-zNrYoS`
- **GLEIF Internal**: `EFcrtYzHx11TElxDmEDx355zm7nJhbmdcIluw7UMbUIL`

### Witnesses (10 total - complete GLEIF production witness set)
- `BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS`
- `BDwydI_FJJ-tvAtCl1tIu_VQqYTI3Q0JyHDhO1v2hZBt`
- `BFl6k3UznzmEVuMpBOtUUiR2RO2NZkR3mKrZkNRaZedo`
- `BGYJwPAzjyJgsipO7GY9ZsBTeoUJrdzjI2w_5N-Nl6gG`
- `BHxz8CDS_mNxAhAxQe1qxdEIzS625HoYgEMgqjZH_g2X`
- `BICY3-X3S3iEsKH73Q1fF_w1JrXJ41V0c4Dn9aQjOSQ-`
- `BLmvLSt1mDShWS67aJNP4gBVBhtOc3YEu8SytqVSsyfw`
- `BLo6wQR73-eH5v90at_Wt8Ep_0xfz05qBjM3_B1UtKbC`
- `BM4Ef3zlUzIAIx-VC8mXziIbtj-ZltM8Aor6TZzmTldj`
- `BNfDO63ZpGc3xiFb0-jIOUnbr_bA-ixMva5cZb3s4BHB`

### Schemas (8 total - complete vLEI schema set)
- **LegalEntityvLEICredential**: `ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY`
- **QualifiedvLEIIssuervLEICredential**: `EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao`
- **OORAuthorizationvLEICredential**: `EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E`
- **ECRAuthorizationvLEICredential**: `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g`
- **LegalEntityOfficialOrganizationalRolevLEICredential**: `EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy`
- **LegalEntityEngagementContextRolevLEICredential**: `EEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw`
- **iXBRLDataAttestation**: `EMhvwOlyEJ9kN4PrwCpr9Jsv7TxPhiYveZ0oP3lJzdEi`
- **iXBRLDataAttestationSchema**: `EOxm1erpuJtjy9bBWO6Wgp9iggefDTNsM6DpO8-jUKbU`

## Testing with the vLEI Server

The vLEI server includes a `WellKnownEnd` handler that serves these resources:

```python
from vlei.app.well_known import loadWellKnownEnds

# In your server setup
oobi_dir = "./samples/oobis/.well-known/keri/oobi"
loadWellKnownEnds(app, oobi_dir)
```

## References

- [GLEIF Well-Known Implementation](https://github.com/GLEIF-IT/GLEIF-IT.github.io/tree/main/.well-known)
- [GLEIF Live Site](https://gleif-it.github.io/.well-known/)
- [RFC 8615: Well-Known URIs](https://www.rfc-editor.org/rfc/rfc8615.html)
- [KERI Specification](https://trustoverip.github.io/kswg-keri-specification/)
- [CESR Specification](https://trustoverip.github.io/kswg-cesr-specification/)

## Migration from Old Format

The old `samples/oobis/` directory contained simple text files with OOBI URLs:
- `gleif-root` → URL string
- `gleif-external` → URL string  
- `gleif-internal` → URL string

The new structure provides:
- Full RFC 8615 compliance with `/.well-known/` path prefix
- Structured JSON indexes for discovery
- Per-identifier directories with KERI message content
- JSON Schema validation
- Support for AIDs, witnesses, and schemas
