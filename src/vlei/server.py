# -*- encoding: utf-8 -*-
"""
server module

"""
import argparse

import falcon
from hio.base import doing
from hio.core import http

from vlei.app import serving

parser = argparse.ArgumentParser(description="Runs vLEI schema server")
parser.add_argument('-p', '--http',
                    action='store',
                    default=7723,
                    help="Port on which to serve vLEI schema SADs.  Defaults to 7723")
parser.add_argument('-d', '--schema-dir',
                    action='store', dest="schemaDir",
                    required=True,
                    help="Port on which to serve vLEI schema SADs.  Defaults to 7723")


def launch(args):
    app = falcon.App()
    server = http.Server(port=args.http, app=app)
    httpServerDoer = http.ServerDoer(server=server)

    serving.loadEnds(app, args.schemaDir)

    doers = [httpServerDoer]

    tock = 0.03125
    doist = doing.Doist(limit=0.0, tock=tock, real=True)
    doist.do(doers=doers)


def main():
    args = parser.parse_args()
    launch(args)


if __name__ == "__main__":
    main()