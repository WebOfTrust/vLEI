```mermaid
sequenceDiagram
    participant G as GLEIF
    participant QVI as QVI
    participant LE as LE
    participant P as Person

    G ->> QVI: Issue QVI vLEI
    Note right of G: Issue to Multisig QVI AID
    
    
    Note over G,QVI: Contains: LEI

```