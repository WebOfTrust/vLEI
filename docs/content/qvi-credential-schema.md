# Qualified vLEI Issuer (QVI) Credential Schema

## Schema Details

The QVI credential is the foundational credential in the vLEI ecosystem, issued directly by GLEIF to Qualified vLEI Issuers. This credential authorizes QVIs to issue Legal Entity vLEI credentials to organizations.

- **Schema SAID**: `EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao`
- **Version**: 1.0.0
- **Issuer**: GLEIF (Global Legal Entity Identifier Foundation)
- **Holder**: Qualified vLEI Issuer (QVI)

## Key Characteristics

- **Direct GLEIF Issuance**: Only GLEIF can issue QVI credentials
- **Delegation**: GLEIF MUST delegate the QVI AID
- **LEI Requirement**: QVI must have a valid Legal Entity Identifier
- **Status Registry**: Transaction Event Log maintains issuance status

```mermaid
classDiagram
    class QualifiedvLEIIssuerCredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : GLEIF Issuee AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +a : Attributes
        +r : Rules
    }

    class Attributes {
        +string d : Attributes block SAID
        +string i : QVI Issuee AID
        +string dt : Issuance date time
        +string LEI : LEI of Legal Entity
        +int gracePeriod : Allocated grace period (default: 90)
    }

    class Rules {
        +string d : Rules block SAID
        +UsageDisclaimer usageDisclaimer
        +IssuanceDisclaimer issuanceDisclaimer
    }

    class UsageDisclaimer {
        +string l : Legal language about usage
    }

    class IssuanceDisclaimer {
        +string l : Legal language about issuance
    }

    QualifiedvLEIIssuerCredential --> "1" Attributes : contains
    QualifiedvLEIIssuerCredential --> "1" Rules : contains
    Rules --> "1" UsageDisclaimer : has
    Rules --> "1" IssuanceDisclaimer : has

    note for QualifiedvLEIIssuerCredential "Schema ID: EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao\nVersion: 1.0.0\nIssued by GLEIF to QVIs"
    
    note for Attributes "Can be either:\n- SAID string reference\n- Full object with properties\nRequired: i, dt, LEI"
    
    note for Rules "Can be either:\n- SAID string reference\n- Full object with disclaimers"
```
