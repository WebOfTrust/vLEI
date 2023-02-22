# -*- encoding: utf-8 -*-
"""
SaidifySchema module

"""
import argparse
import json
import os
import falcon
from hio.base import doing
from hio.core import http
from keri.core import coring, scheming

from vlei.app import generating

parser = argparse.ArgumentParser(description="Saidify schema json file and add to schema directory")
parser.add_argument('--file', '-f',
                    default="",
                    required=True,
                    help='file path of schema file(JSON) to saidify')
parser.add_argument('-s', '--schema-dir',
                    action='store', dest="schemaDir",
                    default="schema/acdc",                    
                    help="Directory of schemas to store schema file")


def saidify(args):
    ff = open(args.file, 'r')
    jsn = json.load(ff)
    ff.close()
    sad = generating.populateSAIDS(jsn)
    schemer = scheming.Schemer(sed=sad)

    s = open(args.file, 'w')
    s.write(json.dumps(schemer.sed, indent=2))
    
    rootDir = os.path.abspath(os.curdir)    
    fileName = os.path.basename(args.file)
    f = open(os.path.join(rootDir, args.schemaDir ,fileName), "w")
    f.write(json.dumps(schemer.sed, indent=2))    
    f.close()


def main():
    args = parser.parse_args()
    saidify(args)


if __name__ == "__main__":
    main()