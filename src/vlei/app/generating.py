from keri.core import coring


def populateSAIDS(d: dict, idage: str = coring.Saids.dollar, code: str = coring.MtrDex.Blake3_256):
    if 'properties' in d:
        props = d['properties']

        # check for top level ids
        for v in ["a", "e", "r"]:
            if v in props and '$id' in props[v]:
                vals = props[v]
                vals[idage] = coring.Saider(sad=vals, code=code, label=idage).qb64
            elif v in props and 'oneOf' in props[v]:
                if isinstance(props[v]['oneOf'], list):
                    # check each 'oneOf' for an id
                    ones = props[v]['oneOf']
                    for o in ones:
                        if isinstance(o, dict) and idage in o:
                            o[idage] = coring.Saider(sad=o, code=code, label=idage).qb64

    d[idage] = coring.Saider(sad=d, code=code, label=idage).qb64

    return d
