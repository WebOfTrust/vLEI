# -*- encoding: utf-8 -*-
"""
vLEI module

"""
import json
import os
from pathlib import Path

from keri.core import scheming
from vlei.app import generating


def main():
    path = Path(__file__).parent

    schemaCache = cache(f'{path}/../../schema/', dict())

    for f, d in schemaCache.items():
        with open(f, 'w') as s:
            d = generating.populateSAIDS(d)

            schemer = scheming.Schemer(sed=d)
            if "acdc" in f:
                f = open(schemer.said, "wb")
                f.write(schemer.raw)
                f.close()
            s.write(json.dumps(schemer.sed, indent=2))


def cache(path, d):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                with open(os.path.join(root, file), 'r') as f:
                    d[os.path.join(root, file)] = json.load(f)

    return d


if __name__ == "__main__":
    main()
