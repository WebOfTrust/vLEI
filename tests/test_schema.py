import json
from pathlib import Path

import pytest
from keri.core import coring, scheming
from keri.kering import ValidationError


@pytest.mark.parametrize("filename", ["verifiable-ixbrl-report-attestation.json",
                                      "legal-entity-official-organizational-role-vLEI-credential.json",
                                      "legal-entity-vLEI-credential.json",
                                      "qualified-vLEI-issuer-vLEI-credential.json",
                                      "oor-authorization-vlei-credential.json",
                                      "ecr-authorization-vlei-credential.json"])
@pytest.mark.parametrize("fmt", ["acdc"])
def test_schema_example(fmt, filename):
    with open(f'{Path(__file__).parent}/../schema/{fmt}/{filename}', 'r') as schema, \
            open(f'{Path(__file__).parent}/../samples/{fmt}/{filename}', 'r') as sample:
        schemer = scheming.Schemer(sed=json.load(schema))

        schemer.verify(sample.read().encode("utf-8"))


@pytest.mark.parametrize("sample", [
    "legal-entity-engagement-context-role-vLEI-credential-auth.json",
    "legal-entity-engagement-context-role-vLEI-credential-le.json",
    "legal-entity-engagement-context-role-vLEI-credential-said.json",
])
@pytest.mark.parametrize("schema", ["legal-entity-engagement-context-role-vLEI-credential.json", ])
@pytest.mark.parametrize("fmt", ["acdc"])
def test_ecr_schema_with_good(fmt, schema, sample):
    with open(f'{Path(__file__).parent}/../schema/{fmt}/{schema}', 'r') as schma, \
            open(f'{Path(__file__).parent}/../samples/acdc/{sample}', 'r') as smple:
        schemer = scheming.Schemer(sed=json.load(schma))

        assert schemer.verify(smple.read().encode("utf-8"))


@pytest.mark.parametrize("sample", [
    "legal-entity-engagement-context-role-vLEI-credential-bad.json",
    "legal-entity-engagement-context-role-vLEI-credential-auth-bad.json",
    "legal-entity-engagement-context-role-vLEI-credential-le-bad.json",
    "legal-entity-engagement-context-role-vLEI-credential-missing-bad.json",
])
@pytest.mark.parametrize("schema", ["legal-entity-engagement-context-role-vLEI-credential.json", ])
@pytest.mark.parametrize("fmt", ["acdc"])
def test_ecr_schema_with_bad(fmt, schema, sample):
    with open(f'{Path(__file__).parent}/../schema/{fmt}/{schema}', 'r') as schma, \
            open(f'{Path(__file__).parent}/../test-vectors/{fmt}/ecr-failures/{sample}', 'r') as smple:
        schemer = scheming.Schemer(sed=json.load(schma))

        with pytest.raises(ValidationError) as e:
            schemer.verify(smple.read().encode("utf-8"))

        assert e.type is ValidationError


def test_legal_entity_chain():
    qvi = json.load(open(f'{__path()}/../schema/acdc/qualified-vLEI-issuer-vLEI-credential.json', 'r'))
    le = json.load(open(f'{__path()}/../schema/acdc/legal-entity-vLEI-credential.json', 'r'))

    assert le['properties']['e']['oneOf'][1]['properties']['qvi']["properties"]['s']['const'] == qvi[coring.Saids.dollar]


def test_ecr_auth_chain():
    auth = json.load(open(f'{__path()}/../schema/acdc/ecr-authorization-vlei-credential.json', 'r'))

    assert auth['properties']['e']['oneOf'][1]['properties']['le']["properties"]['s']['const'] == __le()[
        coring.Saids.dollar]


def test_oor_auth_chain():
    auth = json.load(open(f'{__path()}/../schema/acdc/oor-authorization-vlei-credential.json', 'r'))

    assert auth['properties']['e']['oneOf'][1]['properties']['le']["properties"]['s']['const'] == __le()[
        coring.Saids.dollar]


def test_oor_chain():
    oor = json.load(
        open(f'{__path()}/../schema/acdc/legal-entity-official-organizational-role-vLEI-credential.json',
             'r'))
    auth = json.load(open(f'{Path(__file__).parent}/../schema/acdc/oor-authorization-vlei-credential.json', 'r'))

    assert oor['properties']['e']['oneOf'][1]['properties']['auth']["properties"]['s']['const'] == auth[
        coring.Saids.dollar]


def test_ecr_chain():
    auth = json.load(open(f'{__path()}/../schema/acdc/ecr-authorization-vlei-credential.json', 'r'))
    ecr = json.load(
        open(f'{__path()}/../schema/acdc/legal-entity-engagement-context-role-vLEI-credential.json', 'r'))

    assert ecr['properties']['e']['oneOf'][1]['properties']['auth']["properties"]['s']['const'] == auth[coring.Saids.dollar]
    assert ecr['properties']['e']['oneOf'][2]['properties']['le']["properties"]['s']['const'] == __le()[coring.Saids.dollar]


def __le():
    return json.load(open(f'{__path()}/../schema/acdc/legal-entity-vLEI-credential.json', 'r'))


def __path():
    return Path(__file__).parent
