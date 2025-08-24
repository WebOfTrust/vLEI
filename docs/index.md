---
layout: page
title: "Home"
permalink: /
---

# vLEI Credential Ecosystem Documentation

Welcome to the vLEI (verifiable Legal Entity Identifier) credential ecosystem documentation. This documentation covers the implementation of the GLEIF vLEI ecosystem using KERI (Key Event Receipt Infrastructure) and ACDC (Authentic Chained Data Containers).

## Documentation Overview

### Core Documentation
- [Credentials Overview](credentials/) - Introduction to the credential types and their relationships
- [vLEI Credential Ecosystem](vlei-credential-ecosystem/) - Detailed ecosystem architecture and workflows
- [Dependency Graph](vlei-dependency-graph/) - Visual representation of credential dependencies

### Credential Schemas
- [Auth Credential Schema](auth-credential-schemas/) - ECR and OOR authentication credentials
- [Legal Entity Credential](legal-entity-credential-schema/) - LE credential schema details
- [QVI Credential](qvi-credential-schema/) - Qualified vLEI Issuer credential schema
- [OOR Credential](oor-credential-schema/) - Official Organizational Role credential schema

## Quick Start

The vLEI ecosystem implements a hierarchical trust model for organizational identity verification:

1. **Root of Trust**: GLEIF as the global authority
2. **QVIs**: Qualified vLEI Issuers authorized by GLEIF
3. **Legal Entities**: Organizations with vLEI credentials
4. **Role Holders**: Individuals with official organizational roles

## Key Features

- **Cryptographic Verification**: All credentials are cryptographically verifiable using KERI
- **Chain of Authority**: Clear delegation chains from GLEIF to individual role holders
- **Privacy-Preserving**: Selective disclosure and minimal data exposure
- **Revocation Support**: Built-in credential revocation mechanisms
- **Interoperability**: Standards-based implementation following GLEIF specifications

## Architecture Components

### KERI Infrastructure
- Autonomous Identifier Controllers (AIDs)
- Key Event Logs (KEL)
- Witness Networks
- OOBI (Out-Of-Band-Introduction) resolution

### ACDC Credentials
- Authentic Chained Data Containers
- Schema-based validation
- Cryptographic binding to issuers
- Revocation registries

## Getting Started with Development

This documentation is part of the Kayla wallet implementation. To work with the credential ecosystem:

1. Review the [Credentials Overview](credentials/) to understand the credential types
2. Study the [Ecosystem Documentation](vlei-credential-ecosystem/) for detailed workflows
3. Reference the schema documentation for specific credential implementations
4. Use the [Dependency Graph](vlei-dependency-graph/) to understand credential relationships

## Additional Resources

- [GLEIF vLEI Documentation](https://www.gleif.org/en/lei-solutions/gleifs-digital-strategy-for-the-lei/the-vlei-a-new-future-for-the-lei)
- [KERI Specification](https://github.com/WebOfTrust/keri)
- [ACDC Specification](https://github.com/WebOfTrust/acdc)

## License

This documentation is part of the Kayla wallet project. See the main repository LICENSE file for details.