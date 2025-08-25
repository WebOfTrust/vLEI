---
layout: page
title: "ECR Credential Schema"
permalink: /ecr-credential-schema/
---

# Engagement Context Role (ECR) vLEI Credential Schema

## ECR vLEI Credential Structure

```mermaid
---
config:
  layout: elk
---
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


## Authorization Reference

The ECR vLEI Credential requires an ECR Authorization credential from the Legal Entity. For details on the ECR Authorization structure, see [ECR Auth Credential Schema](/ecr-auth-credential-schema/).

## Key Characteristics

1. **Purpose**: ECR credentials are for specific engagement contexts rather than official organizational positions
2. **Field Names**: Uses `engagementContextRole` for the role description
3. **Use Cases**: Temporary or context-specific interactions, project-based roles, consultancy engagements

## Schema Details

### ECR vLEI Credential
- **Schema SAID**: `EEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw`
- **Version**: 1.0.0
- **Issuer**: QVI (Qualified vLEI Issuer)
- **Recipient**: Person with engagement context role
- **Authorization Required**: ECR Auth credential from LE

### Authorization Requirements
- The QVI must hold a valid ECR Authorization credential from the Legal Entity
- Authorization Schema SAID: `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g`
- See [ECR Auth Credential Schema](/ecr-auth-credential-schema/) for full authorization details

## Credential Flow

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