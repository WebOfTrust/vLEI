# Legal Entity vLEI Credential Schema

```mermaid
classDiagram
    class LegalEntityvLEICredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : QVI Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +a : Attributes
        +e : Edges
        +r : Rules
    }

    class Attributes {
        +string d : Attributes block SAID
        +string i : LE Issuer AID
        +string dt : Issuance date time
        +string LEI : Legal Entity Identifier
    }

    class Edges {
        +string d : Edges block SAID
        +QVINode qvi : QVI reference
    }

    class QVINode {
        +string n : Issuer credential SAID
        +string s : Required schema SAID
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

    LegalEntityvLEICredential --> "1" Attributes : contains
    LegalEntityvLEICredential --> "1" Edges : contains
    LegalEntityvLEICredential --> "1" Rules : contains
    Edges --> "1" QVINode : references
    Rules --> "1" UsageDisclaimer : has
    Rules --> "1" IssuanceDisclaimer : has

    note for LegalEntityvLEICredential "Schema ID: ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY\nVersion: 1.0.0\nIssued by QVI to Legal Entity"
    
    note for Attributes "Can be either:\n- SAID string reference\n- Full object with properties\nRequired: i, dt, LEI"
    
    note for Edges "Links to QVI credential\nSchema: EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao"
    
    note for Rules "Can be either:\n- SAID string reference\n- Full object with disclaimers"
```