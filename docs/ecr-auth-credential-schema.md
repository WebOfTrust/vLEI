---
layout: page
title: "ECR Auth Credential Schema"
permalink: /ecr-auth-credential-schema/
---

# ECR Authorization vLEI Credential Schema

## ECR Authorization vLEI Credential Structure

```mermaid
---
config:
  layout: elk
---
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

## Schema Details

- **Schema SAID**: `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g`
- **Version**: 1.0.0
- **Issuer**: Legal Entity
- **Recipient**: QVI (Qualified vLEI Issuer)
- **Purpose**: Authorize ECR credential issuance for engagement context roles

## Key Characteristics

1. **For engagement-specific or temporary roles**
   - Examples: Project Lead, Consultant, Temporary Representative
   - Context-specific engagements

2. **Required Attributes**:
   - `i`: QVI Issuee AID
   - `dt`: Issuance date time
   - `AID`: Recipient Person AID
   - `LEI`: Legal Entity Identifier
   - `personLegalName`: Recipient name
   - `engagementContextRole`: Engagement context role description

3. **Edge References**:
   - Links to Legal Entity credential
   - Uses I2I (issuer-to-issuer) operator
   - LE Schema: `ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY`

## Authorization Flow

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

The ECR Authorization credential includes:
- **Usage Disclaimer**: Legal language about credential usage
- **Issuance Disclaimer**: Legal language about issuance terms
- **Privacy Disclaimer**: Privacy considerations for IPEX/ACDC usage

The privacy disclaimer is unique to ECR Authorization, recognizing that engagement context roles may require additional privacy considerations for context-specific interactions.

## Differences from OOR Authorization

| Feature | ECR Authorization | OOR Authorization |
|---------|------------------|-------------------|
| **Schema SAID** | `EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g` | `EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E` |
| **Role Field** | `engagementContextRole` | `officialRole` |
| **Privacy Disclaimer** | Yes | No |
| **Use Case** | Context-specific engagements | Permanent organizational roles |