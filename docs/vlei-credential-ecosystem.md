---
layout: page
title: vLEI Credential Ecosystem
permalink: /vlei-credential-ecosystem/
---

# vLEI Credential Ecosystem - Dependencies and Schema Relationships

```mermaid
---
config:
  layout: elk
---
classDiagram
    class QVICredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : GLEIF Issuee AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +Attributes a : Attributes block
        +Rules r : Rules block
    }
    class LECredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : QVI Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +Attributes a : Attributes block
        +Edges e : Edges block
        +Rules r : Rules block
    }
    class OORCredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : QVI Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +Attributes a : Attributes block
        +Edges e : Edges block
        +Rules r : Rules block
    }
    class OORAuthCredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : LE Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +Attributes a : Attributes block
        +Edges e : Edges block
        +Rules r : Rules block
    }
    class ECRAuthCredential {
        +string v : Version
        +string d : Credential SAID
        +string u : One time use nonce
        +string i : LE Issuer AID
        +string ri : Credential status registry
        +string s : Schema SAID
        +Attributes a : Attributes block
        +Edges e : Edges block
        +Rules r : Rules block
    }
    class QVIAttributes {
        +string i : QVI Issuee AID
        +string dt : Issuance date time
        +string LEI : LEI of the requesting Legal Entity
        +int gracePeriod : Allocated grace period
    }
    class LEAttributes {
        +string i : LE Issuer AID
        +string dt : issuance date time
        +string LEI : LE Issuer AID
    }
    class OORAttributes {
        +string i : Person Issuee AID
        +string dt : Issuance date time
        +string LEI : LEI of the Legal Entity
        +string personLegalName : Recipient name as provided during identity assurance
        +string officialRole : Official role title
    }
    class AuthAttributes {
        +string i : QVI Issuee AID
        +string dt : Issuance date time
        +string AID : AID of the intended recipient of the ECR credential
        +string LEI : LEI of the requesting Legal Entity
        +string personLegalName : Requested recipient name as provided during identity assurance
        +string role : Requested role description
    }
    class QVIEdge {
        +string n : Issuer credential SAID
        +string s : SAID of required schema of the credential pointed to by this node
    }
    class LEEdge {
        +string n : Issuer credential SAID
        +string s : SAID of required schema of the credential pointed to by this node
    }
    class AuthEdge {
        +string n : Issuer credential SAID
        +string s : SAID of required schema of the credential pointed to by this node
        +string o : Operator for this edge
    }
    class Rules {
        +UsageDisclaimer usageDisclaimer : Usage Disclaimer
        +IssuanceDisclaimer issuanceDisclaimer : Issuance Disclaimer
        +PrivacyDisclaimer privacyDisclaimer : Privacy Disclaimer
    }
    QVICredential --> QVIAttributes : contains
    QVICredential --> Rules : has
    LECredential --> LEAttributes : contains
    LECredential --> QVIEdge : chains to
    LECredential --> Rules : has
    OORCredential --> OORAttributes : contains
    OORCredential --> AuthEdge : authorized by
    OORCredential --> Rules : has
    OORAuthCredential --> AuthAttributes : contains
    OORAuthCredential --> LEEdge : chains to
    OORAuthCredential --> Rules : has
    ECRAuthCredential --> AuthAttributes : contains
    ECRAuthCredential --> LEEdge : chains to
    ECRAuthCredential --> Rules : has
    LECredential ..> QVICredential : requires - QVI must exist
    OORCredential ..> OORAuthCredential : requires - needs authorization
    OORAuthCredential ..> LECredential : requires - LE must exist
    ECRAuthCredential ..> LECredential : requires - LE must exist
    note for QVICredential "QVI vLEI Credential<br/>Schema: EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao<br/>Issued by: GLEIF → QVI"
    note for LECredential "Legal Entity vLEI Credential<br/>Schema: ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY<br/>Issued by: QVI → LE"
    note for OORCredential "Official Organizational Role<br/>Schema: EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy<br/>Issued by: QVI → Person"
    note for OORAuthCredential "OOR Authorization<br/>Schema: EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E<br/>Issued by: LE → QVI"
    note for ECRAuthCredential "ECR Authorization<br/>Schema: EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g<br/>Issued by: LE → QVI"

```

## Credential Issuance Flow

```mermaid
sequenceDiagram
    participant GLEIF
    participant QVI as Qualified vLEI Issuer
    participant LE as Legal Entity
    participant Person as Person/Role Holder
    
    rect rgb(240, 240, 255)
        Note over GLEIF,QVI: Foundation Layer
        GLEIF->>QVI: Issue QVI vLEI Credential
        Note right of QVI: Schema: EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao
    end
    
    rect rgb(240, 255, 240)
        Note over QVI,LE: Legal Entity Layer
        QVI->>LE: Issue LE vLEI Credential
        Note right of LE: Schema: ENPXp1vQzRF6JwIuS-mp2U8Uf1MoADoP_GqQ62VsDZWY
        Note right of LE: Chains to QVI credential
    end
    
    rect rgb(255, 240, 240)
        Note over LE,Person: Authorization Layer
        LE->>QVI: Issue OOR Authorization
        Note left of QVI: Schema: EKA57bKBKxr_kN7iN5i7lMUxpMG-s19dRcmov1iDxz-E
        Note left of QVI: Authorizes role issuance
        
        LE->>QVI: Issue ECR Authorization
        Note left of QVI: Schema: EH6ekLjSr8V32WyFbGe1zXjTzFs9PkTYmupJ9H65O14g
        Note left of QVI: Authorizes context role
    end
    
    rect rgb(255, 255, 240)
        Note over QVI,Person: Role Credential Layer
        QVI->>Person: Issue OOR vLEI Credential
        Note right of Person: Schema: EBNaNu-M9P5cgrnfl2Fvymy4E_jvxxyjb70PRtiANlJy
        Note right of Person: Chains to OOR Auth
        QVI->>Person: Issue ECR vLEI Credential
        Note right of Person: Schema: EEEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw
        Note right of Person: Chains to ECR Auth
        LE->>Person: Issue ECR vLEI Credential
        Note right of Person: Schema: EEEy9PkikFcANV1l7EHukCeXqrzT1hNZjGlUk7wuMO5jw
    end
```

## Key Design Patterns

### 1. Credential Chaining

- Each credential (except QVI) references its chained credentials through edges
- Ensures verifiable chain of authority from GLEIF down to individual roles

### 2. Compact credentials

- Attributes and Rules can be either:
  - Full objects with all properties
  - SAIDs for compactness

### 3. Common Rules Structure

- All credentials share similar disclaimer structure
- ECR Authorization adds privacy disclaimer for IPEX/ACDC

### 4. Authorization Pattern

- Legal Entities authorize QVIs to issue role credentials
- Separates OOR (official roles) from ECR (engagement context roles)

### 5. Legal Entities as issues

- Legal Entities can issue their own ECR credentials without a preceeding auth
