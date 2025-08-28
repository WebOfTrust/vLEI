# OOR Authorization vLEI Credential Schema

## Schema Details

The OOR Authorization credential is issued by Legal Entities to QVIs, authorizing them to issue OOR credentials for official organizational roles within the organization.

- **Schema SAID**: `EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E`
- **Version**: 1.0.0
- **Issuer**: Legal Entity
- **Holder**: Qualified vLEI Issuer (QVI)
- **Purpose**: Authorize OOR credential issuance for official organizational roles

## Key Characteristics

- **Official Positions**: For permanent, formal organizational roles (CEO, CFO, Director, Manager)
- **Person Specification**: Includes AID and legal name of intended recipient
- **Role Description**: Specifies the official organizational role
- **Formal Hierarchy**: Represents official organizational structure
- **Edge Chaining**: Links to Legal Entity's vLEI credential

## Authorization Flow

### Issuance Process

```mermaid
sequenceDiagram
    participant LE as Legal Entity
    participant QVI as QVI
    participant Person as Person

    rect rgb(240, 240, 255)
        Note over LE,QVI: OOR Authorization Flow
        LE->>QVI: Issue OOR Authorization
        Note over QVI: Schema: EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E
        Note over QVI: Authorizes official role issuance
    end
    
    rect rgb(255, 240, 240)
        Note over QVI,Person: Credential Issuance
        QVI->>Person: Issue OOR Credential
        Note over Person: Based on received authorization
    end
```

## Rules and Disclaimers

The OOR Authorization credential includes two disclaimer types:

- **Usage Disclaimer**: Legal language about credential usage rights and limitations
- **Issuance Disclaimer**: Terms and conditions for credential issuance

Note: Unlike ECR Authorization, OOR Authorization does not include a privacy disclaimer as it is intended for official organizational roles that are typically public.

```mermaid
classDiagram
    class OORAuthvLEICredential {
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

    class OORAuthAttributes {
        +string d : Attributes block SAID
        +string i : QVI Issuee AID
        +string dt : Issuance date time
        +string AID : Recipient AID
        +string LEI : Legal Entity Identifier
        +string personLegalName : Recipient name
        +string officialRole : Role description
    }

    class OORAuthEdges {
        +string d : Edges block SAID
        +LENode le : Legal Entity reference
    }

    class LENode {
        +string n : LE credential SAID
        +string s : Required schema SAID
        +string o : Operator (I2I)
    }

    class OORAuthRules {
        +string d : Rules block SAID
        +UsageDisclaimer usageDisclaimer
        +IssuanceDisclaimer issuanceDisclaimer
    }

    class UsageDisclaimer {
        +string l : Legal language
    }

    class IssuanceDisclaimer {
        +string l : Legal language
    }

    OORAuthvLEICredential --> "1" OORAuthAttributes : contains
    OORAuthvLEICredential --> "1" OORAuthEdges : contains
    OORAuthvLEICredential --> "1" OORAuthRules : contains
    OORAuthEdges --> "1" LENode : references
    OORAuthRules --> "1" UsageDisclaimer : has
    OORAuthRules --> "1" IssuanceDisclaimer : has

    note for OORAuthvLEICredential "Schema ID: EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E\nVersion: 1.0.0\nIssued by LE to QVI\nAuthorizes OOR credential issuance"
    
    note for OORAuthAttributes "Required fields:\ni (QVI AID), dt, AID (Person),\nLEI, personLegalName, officialRole"
    
    note for LENode "Links to LE credential\nSchema: ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY\nOperator: I2I (issuer to issuer)"
```
