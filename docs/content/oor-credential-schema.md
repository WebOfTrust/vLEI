# Legal Entity Official Organizational Role (OOR) vLEI Credential Schema

## Schema Details

The OOR vLEI credential represents official organizational roles within a legal entity. These credentials are issued by QVIs to individuals holding formal positions in an organization.

- **Schema SAID**: `EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy`
- **Version**: 1.0.0
- **Issuer**: Qualified vLEI Issuer (QVI)
- **Holder**: Individual with official organizational role
- **Authorization Required**: OOR Auth credential from Legal Entity

## Key Characteristics

- **Official Positions**: For formal organizational roles (CEO, CFO, Director, etc.)
- **LEI Binding**: Tied to organization's Legal Entity Identifier
- **Authorization Chain**: Requires OOR Auth from Legal Entity to QVI
- **Person Identification**: Links to individual's Autonomic Identifier (AID)
- **Role Specificity**: Uses `officialRole` field for position title

## Authorization Reference

The OOR vLEI Credential requires an OOR Authorization credential from the Legal Entity. This authorization allows the QVI to issue OOR credentials on behalf of the organization.

- **Auth Schema SAID**: `EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E`
- **Auth Type**: Issuer-to-Issuer (I2I) delegation
- See [OOR Auth Credential Schema](oor-auth-credential-schema) for details

## Issuance Process

```mermaid
sequenceDiagram
    participant LE as Legal Entity
    participant QVI as QVI
    participant Person as Person

    LE->>QVI: Issue OOR Authorization
    Note over QVI: See OOR Auth Schema documentation
    
    QVI->>Person: Issue OOR vLEI Credential
    Note over Person: Schema: EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy
    Note over Person: Chains to OOR Auth via edges.auth
```

```mermaid
classDiagram
    class OORvLEICredential {
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
        +string i : Person Issuee AID
        +string dt : Issuance date time
        +string LEI : Legal Entity Identifier
        +string personLegalName : Recipient name
        +string officialRole : Official role title
    }

    class Edges {
        +string d : Edges block SAID
        +AuthNode auth : Authorization chain
    }

    class AuthNode {
        +string n : ACDC SAID reference
        +string s : Required schema SAID
        +string o : Operator (I2I)
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

    OORvLEICredential --> "1" Attributes : contains
    OORvLEICredential --> "1" Edges : contains
    OORvLEICredential --> "1" Rules : contains
    Edges --> "1" AuthNode : references
    Rules --> "1" UsageDisclaimer : has
    Rules --> "1" IssuanceDisclaimer : has

    note for OORvLEICredential "Schema ID: EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy\nVersion: 1.0.0\nIssued by QVI to Official Representatives"
    
    note for Attributes "Required fields:\ni, dt, LEI, personLegalName, officialRole"
    
    note for AuthNode "Links to Auth credential\nSchema: EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E\nOperator: I2I (issuer to issuer)"
    
    note for Rules "Standard vLEI disclaimers\nSame as other vLEI credentials"
```
