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


class WellknownEnd:
    wellknowns = {
        "gleif-root": "http://127.0.0.1:5642/oobi/E4tEHaAAg8LbvdyUwxchP9WO_lZ2vtXyyFFKmTxVGY9U/witness"
                      "/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo",
        "gleif-external": "http://127.0.0.1:5642/oobi/EWN6BzdXo6IByOsuh_fYanK300iEOrQKf6msmbIeC4Y0/witness"
                          "/BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo"
    }

    def on_get(self, req, rep, alias):
        """

        Parameters:
          req (Request): HTTP Request Object
          rep (Response): HTTP Response Object
          alias (str): Alias of Well-Known OOBI

        """

        if alias not in self.wellknowns:
            raise falcon.HTTPBadRequest(title="Unknown well known")

        url = self.wellknowns[alias]
        raise falcon.HTTPMovedPermanently(location=url)


def loadEnds(app, schemaDir, credDir):
    sink = http.serving.StaticSink(staticDirPath="./static")
    app.add_sink(sink, prefix=sink.DefaultStaticSinkBasePath)

    schemaEnd = SchemaEnd(schemaDir=schemaDir, credDir=credDir)
    app.add_route("/oobi/{said}", schemaEnd)

    wellknownEnd = WellknownEnd()
    app.add_route("/.well-known/keri/oobi/{alias}", wellknownEnd)
