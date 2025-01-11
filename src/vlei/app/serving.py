# -*- encoding: utf-8 -*-
"""
vLEI.serving module

"""
import os
from pathlib import Path

import falcon
from hio.core import http
from keri import help

from vlei.app import caching

logger = help.ogler.getLogger()

class ACDCMaterialEnd:
    """Returns ACDC credential schemas or ACDC credentials on HTTP GET"""

    def __init__(self, schemaDir, credDir):
        self.schemaCache = caching.cacheSchema(schemaDir, dict())
        if len(self.schemaCache) == 0:
            logger.error(f"WARNING: No schemas found in schemaDir {schemaDir}")

        self.credentialCache = caching.cacheCredential(credDir, dict())
        if len(self.credentialCache) == 0:
            logger.error(f"WARNING: No credentials found in credDir {credDir}")

    def on_get(self, _, rep, said):
        """
        Returns either ACDC JSON Schema or ACDC Credential if the key (SAID) is in the cache.
        The cache is loaded on startup with the -s (schema) and -c (credentials) arguments.
        """
        if said in self.schemaCache:
            data = self.schemaCache[said]

            rep.status = falcon.HTTP_200
            rep.content_type = "application/schema+json"
            rep.data = data
            return

        if said in self.credentialCache:
            data = self.credentialCache[said]

            rep.status = falcon.HTTP_200
            rep.content_type = "application/acdc+json"
            rep.data = data.encode("utf-8")
            return


class WellKnownEnd:
    """
    Returns well known OOBI URLs on HTTP GET in the Location header as a HTTP 301 redirect.
    The well known OOBI URLs are text files stored in the directory specified by the oobiDir argument.
    The file name is the alias of the well known OOBI and the content of the file is the URL.
    """
    def __init__(self, oobiDir):
        self.oobiDir = oobiDir
        for root, dirs, files in os.walk(oobiDir):
            for file in files:
                p = Path(oobiDir, file)
                url = p.open().read()
                logger.info(f"serving well known {file}: {url}")

    def on_get(self, req, rep, alias):
        """
        Returns the URL of the well known OOBI in the Location header as a HTTP 301 redirect

        Parameters:
          req (Request): HTTP Request Object
          rep (Response): HTTP Response Object
          alias (str): Alias of Well-Known OOBI
        """
        p = Path(self.oobiDir, alias)
        if not p.exists():
            raise falcon.HTTPBadRequest(title="Unknown well known")

        url = p.open().read()
        raise falcon.HTTPMovedPermanently(location=url)


def loadEnds(app, schemaDir, credDir, oobiDir):
    sink = http.serving.StaticSink(staticDirPath="./static")
    app.add_sink(sink, prefix=sink.DefaultStaticSinkBasePath)

    schemaEnd = ACDCMaterialEnd(schemaDir=schemaDir, credDir=credDir)
    app.add_route("/oobi/{said}", schemaEnd)

    wellknownEnd = WellKnownEnd(oobiDir)
    app.add_route("/.well-known/keri/oobi/{alias}", wellknownEnd)
