# -*- encoding: utf-8 -*-
"""
vLEI.serving module

"""
import os
from pathlib import Path

import falcon
from hio.core import http
from keri import help
from keri.help import nowIso8601

from vlei.app import caching, well_known

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

class HealthEnd:
    """Health resource for determining that a container is live"""

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.media = {"message": f"Health is okay. Time is {nowIso8601()}"}

def loadEnds(app, schemaDir, credDir, oobiDir):
    sink = http.serving.StaticSink(staticDirPath="./static")
    app.add_sink(sink, prefix=sink.DefaultStaticSinkBasePath)

    schemaEnd = ACDCMaterialEnd(schemaDir=schemaDir, credDir=credDir)
    app.add_route("/oobi/{said}", schemaEnd)

    well_known.loadWellKnownEnds(app, oobiDir)

    healthEnd = HealthEnd()
    app.add_route("/health", healthEnd)
