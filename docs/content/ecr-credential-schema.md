# Engagement Context Role (ECR) vLEI Credential Schema

## Schema Details

The ECR vLEI credential represents engagement context roles for individuals operating in specific project or consultancy contexts within or on behalf of a legal entity.

- **Schema SAID**: `EEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw`
- **Version**: 1.0.0
- **Issuer**: Qualified vLEI Issuer (QVI)
- **Holder**: Individual with engagement context role
- **Authorization Required**: ECR Auth credential from Legal Entity

## Key Characteristics

- **Context-Specific**: For temporary or project-based engagements
- **Flexible Roles**: Uses `engagementContextRole` field for role description
- **Authorization Chain**: Requires ECR Auth from Legal Entity to QVI
- **LEI Binding**: Tied to organization's Legal Entity Identifier
- **Use Cases**: Consultancy, contractor roles, project teams, external engagements

## Authorization Reference

The ECR vLEI Credential requires an ECR Authorization credential from the Legal Entity. This authorization allows the QVI to issue ECR credentials for specific engagement contexts.

- **Auth Schema SAID**: `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g`
- **Auth Type**: Issuer-to-Issuer (I2I)
- See [ECR Auth Credential Schema](ecr-auth-credential-schema) for details

## Issuance Process

```mermaid
sequenceDiagram
    participant LE as Legal Entity
    participant QVI as QVI
    participant Person as Person

    LE->>QVI: Issue ECR Authorization
    Note over QVI: See ECR Auth Schema documentation
    
    QVI->>Person: Issue ECR vLEI Credential
    Note over Person: Schema: EEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw
    Note over Person: Chains to ECR Auth via edges.auth
```

```mermaid
classDiagram
    class ECRvLEICredential {
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
        +string engagementContextRole : Engagement role title
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

    ECRvLEICredential --> "1" Attributes : contains
    ECRvLEICredential --> "1" Edges : contains
    ECRvLEICredential --> "1" Rules : contains
    Edges --> "1" AuthNode : references
    Rules --> "1" UsageDisclaimer : has
    Rules --> "1" IssuanceDisclaimer : has

    note for ECRvLEICredential "Schema ID: EEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw\nVersion: 1.0.0\nIssued by QVI to Engagement Context Representatives"
    
    note for Attributes "Required fields:\ni, dt, LEI, personLegalName, engagementContextRole"
    
    note for AuthNode "Links to ECR Auth credential\nSchema: EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g\nOperator: I2I (issuer to issuer)"
    
    note for Rules "Standard vLEI disclaimers\nSame as other vLEI credentials"
```
