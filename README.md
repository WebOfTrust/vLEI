# vLEI

## Public Open Specifications for GLEIF vLEI (verifiable Legal Entity Identifiers)

[GLEIF](https://www.gleif.org/en/)

[vLEI](https://www.gleif.org/en/lei-solutions/gleifs-digital-strategy-for-the-lei/introducing-the-verifiable-lei-vlei)

The vLEI is a open standard type of W3C Verifiable Credential (VC) that leverages the W3C Decentralized Identifier (DID) standard. The DID method is `did:keri` which is based onthe [KERI](https://keri.one) identifier system .

### Credential Schema and vLEI Samples
The table below lists all the vLEI credentials with links to the JSON Schema for each credential as well as links to a sample for each:
| Acronym | Full Name of Credential | Link to JSON Schema | Link to Sample Credential JSON |
|---|---|---|---|
| QVI | Qualified vLEI Issuer vLEI Credential | [QVI Schema](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/schema/acdc/qualified-vLEI-issuer-vLEI-credential.json) | [QVI Sample](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/samples/acdc/qualified-vLEI-issuer-vLEI-credential.json) |
| LE | Legal Entity vLEI Credential | [LE Schema](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/schema/acdc/legal-entity-vLEI-credential.json) | [LE Sample](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/samples/acdc/legal-entity-vLEI-credential.json) |
| OOR | Legal Entity Official Organizational Role vLEI Credential | [OOR Schema](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/schema/acdc/legal-entity-official-organizational-role-vLEI-credential.json) | [OOR Sample](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/samples/acdc/legal-entity-official-organizational-role-vLEI-credential.json) |
| ECR | Legal Entity Engagement Context Role vLEI Credential | [ECR Schema](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/schema/acdc/legal-entity-engagement-context-role-vLEI-credential.json) | [ECR Sample](https://github.com/WebOfTrust/vLEI/blob/267c6c7720902eb0e43b0fcc8d9b5f2f63fd5bfa/samples/acdc/legal-entity-engagement-context-role-vLEI-credential.json) | 


### Development

To verify Schema match the samples run:

```shell
pytest
```

To generate new SAIDs for updates schema run:

```shell
python3 src/vlei/generate.py
```

