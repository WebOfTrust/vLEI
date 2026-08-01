# vLEI Server

Verifiable Legal Entity Identifier Schema Generator and Server

| main                                      | dev                                      |
|-------------------------------------------|------------------------------------------|
| [![main][badge-main]][github-actions]     | [![dev][badge-dev]][github-actions]      |
| [![codecov][badge-codecov-main]][codecov] | [![codecov][badge-codecov-dev]][codecov] |


## Public Open Specifications for GLEIF vLEI (verifiable Legal Entity Identifiers)

[GLEIF][gleif]

[vLEI][vlei]

The vLEI is a open standard type of W3C Verifiable Credential (VC) that leverages the W3C Decentralized Identifier (DID) standard. The DID method is `did:keri` which is based onthe [KERI][keri] identifier system .

### Credential Schema and vLEI Samples
The table below lists all the vLEI credentials with links to the JSON Schema for each credential as well as links to a sample for each:

| Acronym  | Full Name of Credential                                   | Link to JSON Schema                | Link to Sample Credential JSON     |
|----------|-----------------------------------------------------------|------------------------------------|------------------------------------|
| QVI      | Qualified vLEI Issuer vLEI Credential                     | [QVI Schema][qvi-schema]           | [QVI Sample][qvi-sample]           |
| LE       | Legal Entity vLEI Credential                              | [LE Schema][le-schema]             | [LE Sample][le-sample]             |
| OOR AUTH | Qualified vLEI Issuer OOR Authorization vLEI Credential   | [OOR AUTH Schema][oor-auth-schema] | [OOR AUTH Sample][oor-auth-sample] |
| ECR AUTH | Qualified vLEI Issuer OOR vLEI Credential                 | [ECR AUTH Schema][ecr-auth-schema] | [ECR AUTH Sample][ecr-auth-sample] |
| OOR      | Legal Entity Official Organizational Role vLEI Credential | [OOR Schema][oor-schema]           | [OOR Sample][oor-sample]           |
| ECR      | Legal Entity Engagement Context Role vLEI Credential      | [ECR Schema][ecr-schema]           | [ECR Sample][ecr-sample]           |


### Development

To verify Schema match the samples run:

```shell
pytest
```

To generate new SAIDs for updates schema run:

```shell
python3 src/vlei/generate.py
```

To Saidify a schema json file and add the schema to ./schema/acdc folder, run:

```shell
saidify-schema -f <file path of schema file(JSON) to saidify>
```

[badge-main]: https://github.com/webOfTrust/vLEI/actions/workflows/test.yml/badge.svg?branch=main
[badge-dev]: https://github.com/webOfTrust/vLEI/actions/workflows/test.yml/badge.svg?branch=dev
[badge-codecov-main]: https://codecov.io/gh/WebOfTrust/vLEI/branch/main/graph/badge.svg?token=C30E9WBW4D
[badge-codecov-dev]: https://codecov.io/gh/WebOfTrust/vLEI/branch/dev/graph/badge.svg?token=C30E9WBW4D
[github-actions]: https://github.com/WebOfTrust/vLEI/actions
[codecov]: https://codecov.io/gh/WebOfTrust/vLEI
[gleif]: https://www.gleif.org/en/
[vlei]: https://www.gleif.org/en/lei-solutions/gleifs-digital-strategy-for-the-lei/introducing-the-verifiable-lei-vlei
[keri]: https://keri.one
[qvi-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/qualified-vLEI-issuer-vLEI-credential.json
[qvi-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/qualified-vLEI-issuer-vLEI-credential.json
[le-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/legal-entity-vLEI-credential.json
[le-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/legal-entity-vLEI-credential.json
[oor-auth-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/oor-authorization-vlei-credential.json
[oor-auth-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/oor-authorization-vlei-credential.json
[ecr-auth-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/ecr-authorization-vlei-credential.json
[ecr-auth-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/ecr-authorization-vlei-credential.json
[oor-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/legal-entity-official-organizational-role-vLEI-credential.json
[oor-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/legal-entity-official-organizational-role-vLEI-credential.json
[ecr-schema]: https://github.com/WebOfTrust/vLEI/blob/dev/schema/acdc/legal-entity-engagement-context-role-vLEI-credential.json
[ecr-sample]: https://github.com/WebOfTrust/vLEI/blob/dev/samples/acdc/legal-entity-engagement-context-role-vLEI-credential.json
