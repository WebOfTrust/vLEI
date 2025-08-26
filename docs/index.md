---
layout: page
title: "Home"
permalink: /
---

# vLEI Ecosystem Credential Documentation

This documentation covers the implementation of the GLEIF vLEI ecosystem using KERI (Key Event Receipt Infrastructure) and ACDC (Authentic Chained Data Containers).

## Documentation Overview

### Core Documentation
- [Credentials Overview](/credentials/) - Introduction to the credential types and their relationships
- [vLEI Credential Ecosystem](/vlei-credential-ecosystem/) - Detailed ecosystem architecture and workflows
- [Dependency Graph](/vlei-dependency-graph/) - Visual representation of credential dependencies

### Credential Schemas

- [Auth Credential Schema](/auth-credential-schemas/) - OOR and ECR authorization credentials
- [Legal Entity Credential](/legal-entity-credential-schema/) - LE credential schema details
- [QVI Credential](/qvi-credential-schema/) - Qualified vLEI Issuer credential schema
- [OOR Credential](/oor-credential-schema/) - Official Organizational Role credential schema
- [ECR Credential](/ecr-credential-schema/) - Engagement Context Role credential schema

## Quick Start

The vLEI ecosystem implements a hierarchical trust model for organizational identity verification:

1. **Root of Trust**: GLEIF as the global authority
2. **QVIs**: Qualified vLEI Issuers authorized by GLEIF
3. **Legal Entities**: Organizations with vLEI credentials
4. **Role Holders**: Individuals with official organizational roles

## Key Features

- **Cryptographic Verification**: All credentials are cryptographically end verifiable using KERI
- **Chain of Authority**: Clear delegation chains from GLEIF to individual role holders
- **Privacy-Preserving**: Selective disclosure and compact credentials
- **Revocation Support**: Transaction Event Logs capture issuance state

## SVG Renderings

Some class diagrams render better using ELK but the config doesn't seem to be picked up by Jekyll.

### Available SVG Diagrams

- [Auth Credential Schemas](auth-credential-schemas.svg) - Authorization credential relationships
- [Credentials Issuance Schema](credentials-issuance-schema.svg) - Credential issuance process
- [Credentials Trust Chain](credentials-trust-chain.svg) - Trust chain visualization
- [ECR Auth Credential Schema](ecr-auth-credential-schema.svg) - ECR authorization credential structure
- [ECR Credential Schema](ecr-credential-schema.svg) - Engagement Context Role credential structure
- [Legal Entity Credential Schema](legal-entity-credential-schema.svg) - Legal Entity credential structure
- [OOR Auth Credential Schema](oor-auth-credential-schema.svg) - OOR authorization credential structure
- [OOR Credential Schema](oor-credential-schema.svg) - Official Organizational Role credential structure
- [QVI Credential Schema](qvi-credential-schema.svg) - Qualified vLEI Issuer credential structure
- [vLEI Credential Ecosystem](vlei-credential-ecosystem.svg) - Complete ecosystem overview
- [vLEI Dependency Graph](vlei-dependency-graph.svg) - Credential dependency relationships



## Additional Resources

- [KERI Specification](https://trustoverip.github.io/tswg-keri-specification/)
- [ACDC Specification](https://trustoverip.github.io/tswg-acdc-specification/)
- [CESR Specification](https://trustoverip.github.io/tswg-cesr-specification/)
