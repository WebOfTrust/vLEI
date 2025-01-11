# -*- encoding: utf-8 -*-
"""
vlei.server module
Contains the Doist and Doers comprising the vLEI server.

"""
import argparse
import logging
from dataclasses import dataclass
from typing import List

import falcon
from hio.base import doing, Doer
from hio.core import http, tcp
from keri import help

from vlei.app import serving
from vlei.app.shutdown import GracefulShutdownDoer

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


@dataclass
class VLEIConfig:
    # HTTP port to listen on
    http: int = 7723
    # ACDC schema directory
    schemaDir: str = "./schema/acdc/"
    # ACDC material directory
    credDir: str = "./samples/acdc/"
    # Well known OOBI directory
    oobiDir: str = "./samples/oobis/"
    # TLS key material
    keypath: str = None
    certpath: str = None
    cafilepath: str = None


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

def setupVLEIDoers(config: VLEIConfig):
    """Set up the doers that will be run by the Doist scheduler."""
    app = falcon.App()
    port = int(config.http)
    keypath = config.keypath
    certpath = config.certpath
    cafilepath = config.cafilepath
    if keypath is not None and certpath is not None and cafilepath is not None:
        logger.info(f"vLEI-server starting on port {port} with TLS enabled")
    else:
        logger.info(f"vLEI-server starting on port {port} with TLS disabled")
    server = createHttpServer(port=int(config.http), app=app,
                              keypath=config.keypath, certpath=config.certpath,
                              cafilepath=config.cafilepath)
    if not server.reopen():
        raise RuntimeError(f"cannot create http server on port {int(config.http)}")
    httpServerDoer = http.ServerDoer(server=server)

    serving.loadEnds(app, schemaDir=config.schemaDir, credDir=config.credDir, oobiDir=config.oobiDir)

    doers = [httpServerDoer]
    return doers

def vLEIDoist(doers: List[Doer]):
    """Creates a Doist that will run the vLEI server."""
    tock = 0.03125
    doist = doing.Doist(limit=0.0, tock=tock, real=True)
    doers.append(GracefulShutdownDoer(doist=doist))
    doist.doers = doers
    return doist


def launch(config: VLEIConfig):
    """Launches the vLEI server by calling Doist.do() on the Doers that make up the server."""
    logger.setLevel(logging.INFO)
    doist = vLEIDoist(setupVLEIDoers(config))
    doist.do() # Enters the doist loop until shutdown
    logger.info("vLEI-server stopped")


def main():
    args = parser.parse_args()
    launch(VLEIConfig(
        http=args.http,
        schemaDir=args.schemaDir,
        credDir=args.credDir,
        oobiDir=args.oobiDir,
        keypath=args.keypath,
        certpath=args.certpath,
        cafilepath=args.cafilepath
    ))


if __name__ == "__main__":
    main()
