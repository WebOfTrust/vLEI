# -*- encoding: utf-8 -*-
"""
vLEI.serving module

"""

import falcon
from hio.core import http

from vlei.app import caching


class SchemaEnd:

    def __init__(self, schemaDir, credDir):
        self.schemaCache = caching.cacheSchema(schemaDir, dict())
        self.credentialCache = caching.cacheCredential(credDir, dict())

    def on_get(self, _, rep, said):
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


def loadEnds(app, schemaDir, credDir):

    sink = http.serving.StaticSink(staticDirPath="./static")
    app.add_sink(sink, prefix=sink.DefaultStaticSinkBasePath)

    schemaEnd = SchemaEnd(schemaDir=schemaDir, credDir=credDir)
    app.add_route("/oobi/{said}", schemaEnd)
