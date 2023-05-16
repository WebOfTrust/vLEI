# -*- encoding: utf-8 -*-
"""
vLEI module

"""
import json
import os
from pathlib import Path

from keri.core import scheming, coring
from vlei.app import generating


def main():
    path = Path(__file__).parent

    # qvi
    p = f'{path}/../../schema/acdc/qualified-vLEI-issuer-vLEI-credential.json'
    qvi = __load(p)
    qvi = generating.populateSAIDS(qvi)
    __save(p, qvi)

    # legal entity -> qvi edge
    p = f'{path}/../../schema/acdc/legal-entity-vLEI-credential.json'
    le = __load(p)
    le['properties']['e']['oneOf'][1]['properties']['qvi']["properties"]['s']['const'] = qvi[coring.Ids.dollar]
    le = generating.populateSAIDS(le)
    __save(p, le)

    # oor auth -> le edge
    p = f'{path}/../../schema/acdc/oor-authorization-vlei-credential.json'
    oorAuth = __load(p)
    oorAuth['properties']['e']['oneOf'][1]['properties']['le']["properties"]['s']['const'] = le[coring.Ids.dollar]
    oorAuth = generating.populateSAIDS(oorAuth)
    __save(p, oorAuth)

    # oor -> oor auth edge
    p = f'{path}/../../schema/acdc/legal-entity-official-organizational-role-vLEI-credential.json'
    oor = __load(p)
    oor['properties']['e']['oneOf'][1]['properties']['auth']["properties"]['s']['const'] = oorAuth[coring.Ids.dollar]
    oor = generating.populateSAIDS(oor)
    __save(p, oor)

    # ecr auth -> le edge
    p = f'{path}/../../schema/acdc/ecr-authorization-vlei-credential.json'
    ecrAuth = __load(p)
    ecrAuth['properties']['e']['oneOf'][1]['properties']['le']["properties"]['s']['const'] = le[coring.Ids.dollar]
    ecrAuth = generating.populateSAIDS(ecrAuth)
    __save(p, ecrAuth)

    # ecr -> ecr auth edge and le edge
    p = f'{path}/../../schema/acdc/legal-entity-engagement-context-role-vLEI-credential.json'
    ecr = __load(p)
    ecr['properties']['e']['oneOf'][1]['properties']['auth']["properties"]['s']['const'] = ecrAuth[coring.Ids.dollar]
    ecr['properties']['e']['oneOf'][2]['properties']['le']["properties"]['s']['const'] = le[coring.Ids.dollar]
    ecr = generating.populateSAIDS(ecr)
    __save(p, ecr)

    p = f'{path}/../../schema/acdc/verifiable-ixbrl-report-attestation.json'
    vira = __load(p)
    vira['properties']['e']['oneOf'][0]['properties']['oor']["properties"]['s']['const'] = oor[coring.Ids.dollar]
    vira['properties']['e']['oneOf'][1]['properties']['ecr']["properties"]['s']['const'] = ecr[coring.Ids.dollar]
    vira = generating.populateSAIDS(vira)
    __save(p, vira)

def __load(p):
    ff = open(p, 'r')
    jsn = json.load(ff)
    ff.close()
    return jsn


def __save(p, d):
    schemer = scheming.Schemer(sed=d)
    f = open(schemer.said, "wb")
    f.write(schemer.raw)
    f.close()

    s = open(p, 'w')
    s.write(json.dumps(schemer.sed, indent=2))

    # for github pages
    p = 'publish'
    os.makedirs(os.path.join(p, schemer.said), exist_ok=True)
    f = open(os.path.join(p, schemer.said, 'index.json'), 'wb')
    f.write(schemer.raw)
    f.close()


if __name__ == "__main__":
    main()
