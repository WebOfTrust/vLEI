# ECR Authorization vLEI Credential Schema

## Schema Details

The ECR Authorization credential is issued by Legal Entities to QVIs, authorizing them to issue ECR credentials for specific engagement context roles within the organization.

- **Schema SAID**: `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g`
- **Version**: 1.0.0
- **Issuer**: Legal Entity
- **Holder**: Qualified vLEI Issuer (QVI)
- **Purpose**: Authorize ECR credential issuance for engagement context roles

## Key Characteristics

- **Engagement-Specific**: For temporary, project-based, or consultancy roles
- **Person Specification**: Includes AID and legal name of intended recipient
- **Role Description**: Specifies the engagement context role
- **Privacy Considerations**: Includes privacy disclaimer for IPEX/ACDC usage
- **Edge Chaining**: Links to Legal Entity's vLEI credential

## Authorization Flow

### Issuance Process

```mermaid
sequenceDiagram
    participant LE as Legal Entity
    participant QVI as QVI
    participant Person as Person

    rect rgb(240, 255, 240)
        Note over LE,QVI: ECR Authorization Flow
        LE->>QVI: Issue ECR Authorization
        Note over QVI: Schema: EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g
        Note over QVI: Authorizes engagement context role issuance
        Note over QVI: Includes privacy disclaimer
    end
    
    rect rgb(255, 240, 240)
        Note over QVI,Person: Credential Issuance
        QVI->>Person: Issue ECR Credential
        Note over Person: Based on received authorization
    end
```

## Rules and Disclaimers

The ECR Authorization credential includes three disclaimer types:

- **Usage Disclaimer**: Legal language about credential usage rights and limitations
- **Issuance Disclaimer**: Terms and conditions for credential issuance
- **Privacy Disclaimer**: Privacy considerations for IPEX/ACDC usage (unique to ECR Auth)

The privacy disclaimer is specific to ECR Authorization credentials, acknowledging that engagement context roles may involve external parties requiring additional privacy protections.

```mermaid
classDiagram
    class ECRAuthvLEICredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : LE Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +a : Attributes
        +e : Edges
        +r : Rules
    }

    class ECRAuthAttributes {
        +string d : Attributes block SAID
        +string i : QVI Issuee AID
        +string dt : Issuance date time
        +string AID : Recipient AID
        +string LEI : Legal Entity Identifier
        +string personLegalName : Recipient name
        +string engagementContextRole : Role description
    }

    class ECRAuthEdges {
        +string d : Edges block SAID
        +LENode le : Legal Entity reference
    }

    class LENode {
        +string n : LE credential SAID
        +string s : Required schema SAID
        +string o : Operator (I2I)
    }

    class ECRAuthRules {
        +string d : Rules block SAID
        +UsageDisclaimer usageDisclaimer
        +IssuanceDisclaimer issuanceDisclaimer
        +PrivacyDisclaimer privacyDisclaimer
    }

    class UsageDisclaimer {
        +string l : Legal language
    }

    class IssuanceDisclaimer {
        +string l : Legal language
    }

    class PrivacyDisclaimer {
        +string l : Privacy considerations text
    }

    ECRAuthvLEICredential --> "1" ECRAuthAttributes : contains
    ECRAuthvLEICredential --> "1" ECRAuthEdges : contains
    ECRAuthvLEICredential --> "1" ECRAuthRules : contains
    ECRAuthEdges --> "1" LENode : references
    ECRAuthRules --> "1" UsageDisclaimer : has
    ECRAuthRules --> "1" IssuanceDisclaimer : has
    ECRAuthRules --> "1" PrivacyDisclaimer : has

    note for ECRAuthvLEICredential "Schema ID: EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g\nVersion: 1.0.0\nIssued by LE to QVI\nAuthorizes ECR credential issuance"
    
    note for ECRAuthAttributes "Required fields:\ni (QVI AID), dt, AID (Person),\nLEI, personLegalName, engagementContextRole"
    
    note for LENode "Links to LE credential\nSchema: ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY\nOperator: I2I (issuer to issuer)"
    
    note for PrivacyDisclaimer "ECR Auth includes privacy\nconsiderations for IPEX/ACDC usage"
```
