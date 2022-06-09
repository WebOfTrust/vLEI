# -*- encoding: utf-8 -*-
"""
vLEI.serving module

"""
from pathlib import Path
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


class WellknownEnd:
    def __init__(self, oobiDir):
        self.oobiDir = oobiDir

    def on_get(self, req, rep, alias):
        """

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

    schemaEnd = SchemaEnd(schemaDir=schemaDir, credDir=credDir)
    app.add_route("/oobi/{said}", schemaEnd)

    wellknownEnd = WellknownEnd(oobiDir)
    app.add_route("/.well-known/keri/oobi/{alias}", wellknownEnd)
