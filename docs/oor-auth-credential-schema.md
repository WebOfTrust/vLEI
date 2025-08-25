---
layout: page
title: "OOR Auth Credential Schema"
permalink: /oor-auth-credential-schema/
---

# OOR Authorization vLEI Credential Schema

## OOR Authorization vLEI Credential Structure

```mermaid
---
config:
  layout: elk
---
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

## Schema Details

- **Schema SAID**: `EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E`
- **Version**: 1.0.0
- **Issuer**: Legal Entity
- **Recipient**: QVI (Qualified vLEI Issuer)
- **Purpose**: Authorize OOR credential issuance for official organizational roles

## Key Characteristics

1. **For permanent, official organizational positions**
   - Examples: CEO, CFO, Director, Manager
   - Represents formal organizational hierarchy

2. **Required Attributes**:
   - `i`: QVI Issuee AID
   - `dt`: Issuance date time
   - `AID`: Recipient Person AID
   - `LEI`: Legal Entity Identifier
   - `personLegalName`: Recipient name
   - `officialRole`: Official role description

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

The OOR Authorization credential includes:
- **Usage Disclaimer**: Legal language about credential usage
- **Issuance Disclaimer**: Legal language about issuance terms

Note: Unlike ECR Authorization, OOR Authorization does not include a privacy disclaimer as it is intended for official organizational roles that are typically public.