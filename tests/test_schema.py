import json
from pathlib import Path

import pytest
from keri.core import scheming


@pytest.mark.parametrize("filename", ["verifiable-ixbrl-report-attestation.json",
                                      "legal-entity-engagement-context-role-vLEI-credential.json",
                                      "legal-entity-official-organizational-role-vLEI-credential.json",
                                      "legal-entity-vLEI-credential.json",
                                      "qualified-vLEI-issuer-vLEI-credential.json"])
@pytest.mark.parametrize("fmt", ["acdc"])
def test_schema_example(fmt, filename):
    with open(f'{Path(__file__).parent}/../schema/{fmt}/{filename}', 'r') as schema, \
            open(f'{Path(__file__).parent}/../samples/{fmt}/{filename}', 'r') as sample:
        schemer = scheming.Schemer(sed=json.load(schema))

        schemer.verify(sample.read().encode("utf-8"))
