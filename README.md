# vLEI

## Public Open Specifications for GLEIF vLEI (verifiable Legal Entity Identifiers)

[GLEIF](https://www.gleif.org/en/)

[vLEI](https://www.gleif.org/en/lei-solutions/gleifs-digital-strategy-for-the-lei/introducing-the-verifiable-lei-vlei)

The vLEI is a open standard type of W3C Verifiable Credential (VC) that leverages the W3C Decentralized Identifier (DID) standard. The DID method is `did:keri` which is based onthe [KERI](https://keri.one) identifier system .

### Development

To verify Schema match the samples run:

```shell
pytest
```

To generate new SAIDs for updates schema run:

```shell
python3 src/vlei/generate_said.py
```

