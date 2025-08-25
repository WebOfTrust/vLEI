---
layout: page
title: "Home"
permalink: /
---

# vLEI Ecosystem Credential Documentation

This documentation covers the implementation of the GLEIF vLEI ecosystem using KERI (Key Event Receipt Infrastructure) and ACDC (Authentic Chained Data Containers).

## Documentation Overview

### Core Documentation
- [Credentials Overview](credentials.md) - Introduction to the credential types and their relationships
- [vLEI Credential Ecosystem](vlei-credential-ecosystem.md) - Detailed ecosystem architecture and workflows
- [Dependency Graph](vlei-dependency-graph.md) - Visual representation of credential dependencies

### Credential Schemas
- [Auth Credential Schema](auth-credential-schemas.md) - ECR and OOR authentication credentials
- [Legal Entity Credential](legal-entity-credential-schema.md) - LE credential schema details
- [QVI Credential](qvi-credential-schema.md) - Qualified vLEI Issuer credential schema
- [OOR Credential](oor-credential-schema.md) - Official Organizational Role credential schema

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

## Additional Resources

- [KERI Specification](https://trustoverip.github.io/tswg-keri-specification/)
- [ACDC Specification](https://trustoverip.github.io/tswg-acdc-specification/)
- [CESR Specification](https://trustoverip.github.io/tswg-cesr-specification/)