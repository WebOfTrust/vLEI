# -*- encoding: utf-8 -*-
"""
vLEI.serving module

"""
import falcon

from vlei.app import caching


class SchemaEnd:

    def __init__(self, directory):
        self.schemaCache = caching.cache(directory, dict())

    def on_get(self, _, rep, said):
        if said not in self.schemaCache:
            rep.status = falcon.HTTP_404
            rep.text = f"Schema {said} not found"
            return None

        data = self.schemaCache[said]

        rep.status = falcon.HTTP_200
        rep.content_type = "application/schema+json"
        rep.data = data


def loadEnds(app, directory):

    schemaEnd = SchemaEnd(directory=directory)
    app.add_route("/oobi/{said}", schemaEnd)




