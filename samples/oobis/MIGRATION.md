# Migration to RFC 8615 Compliant Well-Known Structure

## Summary

The `samples/oobis/` directory has been restructured to follow the [GLEIF Well-Known URI Structure Specification](https://github.com/GLEIF-IT/GLEIF-IT.github.io/blob/main/.well-known/STRUCTURE.md) and [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615.html).

## Changes Made

### Old Structure (Deprecated)
```
samples/oobis/
├── gleif-root       # Plain text file with single OOBI URL
├── gleif-external   # Plain text file with single OOBI URL
└── gleif-internal   # Plain text file with single OOBI URL
```

**Backed up to**: `samples/oobis.old/`

### New Structure (RFC 8615 Compliant)
```
samples/oobis/.well-known/
├── index.json                  # Main discovery index
├── schema.json                 # JSON Schema for validation
└── keri/
    └── oobi/
        ├── index.json          # OOBI catalog
        ├── schema.json         # OOBI index schema
        ├── EDP1vHcw_.../       # GLEIF Root AID
        │   └── index.json      # rpy message with witness URLs
        ├── EINmHd5g_.../       # GLEIF External AID
        │   └── index.json      # rpy message with witness URLs
        ├── EFcrtYzHx_.../      # GLEIF Internal AID
        │   └── index.json      # rpy message with witness URLs
        ├── BDkq35LUU_.../      # Sample witness
        │   └── index.json      # Witness KEL (icp + rpy)
        ├── ENPXp1vQz_.../      # LegalEntityvLEICredential schema
        │   └── index.json      # JSON Schema
        └── EBfdlu8R2_.../      # QualifiedvLEIIssuervLEICredential schema
            └── index.json      # JSON Schema
```

## Benefits

1. **RFC 8615 Compliance**: Uses standard `/.well-known/` path prefix
2. **Structured Discovery**: JSON indexes enable programmatic resource discovery
3. **Type Safety**: JSON Schema validation for all indexes
4. **Complete Resource Serving**: 
   - AIDs return full witness set in rpy messages
   - Witnesses return complete KEL
   - Schemas return full JSON Schema definitions
5. **Extensible**: Easy to add new AIDs, witnesses, or schemas

## Implementation

### New Python Module
- **`src/vlei/app/well_known.py`**: RFC 8615 compliant endpoint handler
  - `WellKnownIndex`: Loads and queries index.json
  - `WellKnownEnd`: Falcon endpoint handler
  - `loadWellKnownEnds()`: Helper to register endpoints

## Usage

### Serving Well-Known Resources

```python
from vlei.app.well_known import loadWellKnownEnds
import falcon

app = falcon.App()
oobi_dir = "./samples/oobis/.well-known/keri/oobi"
loadWellKnownEnds(app, oobi_dir)
```

### Discovery Examples

```bash
# Discover all resources
curl http://localhost:7723/.well-known/index.json

# Discover KERI OOBIs
curl http://localhost:7723/.well-known/keri/oobi/index.json

# Get GLEIF Root witness URLs
curl http://localhost:7723/.well-known/keri/oobi/EDP1vHcw_wc4M__Fj53-cJaBnZZASd-aMTaSyWEQ-PC2/index.json

# Get witness KEL
curl http://localhost:7723/.well-known/keri/oobi/BDkq35LUU63xnFmfhljYYRY0ymkCg7goyeCxN30tsvmS/index.json

# Get Legal Entity schema
curl http://localhost:7723/.well-known/keri/oobi/ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY/index.json
```

## Content Types

The handler returns appropriate content types based on identifier type:

| Type | Content-Type | Description |
|------|-------------|-------------|
| AID | `application/cesr` | KERI rpy message with witness URLs |
| Witness | `application/cesr` | Witness KEL (icp + rpy messages) |
| Schema | `application/cesr` | ACDC JSON Schema |

Note: When content is valid JSON, `application/json+cesr` may be used.

## Source Data

All content copied from the live GLEIF implementation:
- Repository: https://github.com/GLEIF-IT/GLEIF-IT.github.io/tree/main/.well-known
- Live site: https://gleif-it.github.io/.well-known/

## References

- [GLEIF Well-Known Structure Spec](https://github.com/GLEIF-IT/GLEIF-IT.github.io/blob/main/.well-known/STRUCTURE.md)
- [GLEIF Well-Known Schema Spec](https://github.com/GLEIF-IT/GLEIF-IT.github.io/blob/main/.well-known/SCHEMA.md)
- [RFC 8615: Well-Known URIs](https://www.rfc-editor.org/rfc/rfc8615.html)
- [KERI Specification](https://trustoverip.github.io/kswg-keri-specification/)
