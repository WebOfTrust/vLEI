# -*- encoding: utf-8 -*-
"""
server module

"""
import argparse
import logging
import signal

import falcon
from hio.base import doing
from hio.core import http, tcp

from keri import help

from vlei.app import serving

parser = argparse.ArgumentParser(description="Runs vLEI schema server")
parser.add_argument('-p', '--http',
                    action='store',
                    default=7723,
                    help="Port on which to serve vLEI schema SADs.  Defaults to 7723")
parser.add_argument('-s', '--schema-dir',
                    action='store', dest="schemaDir",
                    required=True,
                    help="Directory of schema to serve")
parser.add_argument('-c', '--cred-dir',
                    action='store', dest="credDir",
                    required=True,
                    help="Directory of credentials to serve")
parser.add_argument('-o', '--oobi-dir',
                    action='store', dest="oobiDir",
                    required=True,
                    help="Directory of OOBIs to serve")
parser.add_argument("--keypath", action="store", required=False, default=None,
                    help="TLS server private key file")
parser.add_argument("--certpath", action="store", required=False, default=None,
                    help="TLS server signed certificate (public key) file")
parser.add_argument("--cafilepath", action="store", required=False, default=None,
                    help="TLS server CA certificate chain")

logger = help.ogler.getLogger()


def createHttpServer(port, app, keypath=None, certpath=None, cafilepath=None):
    """
    Create an HTTP or HTTPS server depending on whether TLS key material is present

    Parameters:
        port (int)         : port to listen on for all HTTP(s) server instances
        app (falcon.App)   : application instance to pass to the http.Server instance
        keypath (string)   : the file path to the TLS private key
        certpath (string)  : the file path to the TLS signed certificate (public key)
        cafilepath (string): the file path to the TLS CA certificate chain file
    Returns:
        hio.core.http.Server
    """
    if keypath is not None and certpath is not None and cafilepath is not None:
        servant = tcp.ServerTls(certify=False,
                                keypath=keypath,
                                certpath=certpath,
                                cafilepath=cafilepath,
                                port=port)
        server = http.Server(port=port, app=app, servant=servant)
    else:
        server = http.Server(port=port, app=app)
    return server


def launch(args):
    logger.setLevel(logging.INFO)
    app = falcon.App()
    port = int(args.http)
    keypath = args.keypath
    certpath = args.certpath
    cafilepath = args.cafilepath
    if keypath is not None and certpath is not None and cafilepath is not None:
        logger.info(f"vLEI-server starting on port {port} with TLS enabled")
    else:
        logger.info(f"vLEI-server starting on port {port} with TLS disabled")
    server = createHttpServer(port=int(args.http), app=app,
                              keypath=args.keypath, certpath=args.certpath,
                              cafilepath=args.cafilepath)
    if not server.reopen():
        raise RuntimeError(f"cannot create http server on port {int(args.http)}")
    httpServerDoer = http.ServerDoer(server=server)

    serving.loadEnds(app, schemaDir=args.schemaDir, credDir=args.credDir, oobiDir=args.oobiDir)

    doers = [httpServerDoer]

    # Shutdown hook
    def shutdownHandler(sig, frame):
        logger.info("Received signal %s", signal.strsignal(sig))
        doist.exit()
    signal.signal(signal.SIGTERM, shutdownHandler)

    tock = 0.03125
    doist = doing.Doist(limit=0.0, tock=tock, real=True)
    doist.do(doers=doers) # Enters the doist loop until shutdown

    logger.info("vLEI-server stopped")

def main():
    args = parser.parse_args()
    launch(args)


if __name__ == "__main__":
    main()
