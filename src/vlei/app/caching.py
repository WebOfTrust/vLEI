# -*- encoding: utf-8 -*-
"""
vLEI.caching module

"""
import json
import os

from keri.core import scheming


def cacheSchema(path, d):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                with open(os.path.join(root, file), 'r') as f:
                    ked = json.load(f)
                    schemer = scheming.Schemer(sed=ked)
                    print(f"caching schema {schemer.said}")
                    d[schemer.said] = schemer.raw

    return d


def cacheCredential(path, d):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('-acdc.cesr'):
                with open(os.path.join(root, file), 'r') as f:
                    said = file.rstrip('-acdc.cesr')
                    print(f"caching credential {said}")
                    d[said] = f.read()

    return d

