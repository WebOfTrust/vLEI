from vlei.app import generating


def test_schema_said():
    d = \
        {
            "$id": "",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
        }
    d = generating.populateSAIDS(d)

    assert d == {'$id': 'EDQLuhDJVUbyVWg7OW-NVFwTKoVWGjixHD8ZusvNCHbP',
                 '$schema': 'http://json-schema.org/draft-07/schema#',
                 'type': 'object'}


def test_sub_schema_said():
    d = \
        {
            '$id': '',
            '$schema': 'http://json-schema.org/draft-07/schema#',
            'type': 'object',
            'properties': {
                'a': {
                    '$id': '',
                    'description': 'a'
                },
                'e': {
                    '$id': '',
                    'description': 'e'
                },
                'r': {
                    '$id': '',
                    'description': 'r'
                }
            }
        }
    d = generating.populateSAIDS(d)

    assert d == {'$id': 'EGPA1QjwPXoABEyZltm3NF2mbZ55_uEyx0AqBuGjKWFJ',
                 '$schema': 'http://json-schema.org/draft-07/schema#',
                 'properties': {'a': {'$id': 'EGfNqmll8IJLdzH_sQIt7fU-pGTjmcc0g0pik5q-pRoo',
                                      'description': 'a'},
                                'e': {'$id': 'EGBzPDeUuCJyPXzg_-XcgG9g68lLZCBBhbOsNiKJ2t6m',
                                      'description': 'e'},
                                'r': {'$id': 'ECqFQxDi7hm673NivvU_xJNvT1w5sM_y_7HE1jJlCxI-',
                                      'description': 'r'}},
                 'type': 'object'}


def test_sub_schema_one_of_said():
    d = \
        {
            "$id": "",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties":
                {
                    "a": {
                        "oneOf": [
                            {
                                "description": "Attributes block SAID",
                                "type": "string"
                            },
                            {
                                "$id": "",
                                "description": "Attributes block",
                            },
                        ]
                    },
                    "e": {
                        "oneOf": [
                            {
                                "description": "Edges block SAID",
                                "type": "string"
                            },
                            {
                                "$id": "",
                                "description": "Edges block",
                            },
                        ]
                    },
                    "r": {
                        "oneOf": [
                            {
                                "description": "Rules block SAID",
                                "type": "string"
                            },
                            {
                                "$id": "",
                                "description": "Rules block",
                            },
                        ]
                    }
                }
        }
    d = generating.populateSAIDS(d)

    assert d == {'$id': 'EGMcqtFTjdf4Jb-xHuv1mvKqpNvuH_BwrlrvQQbD40dy',
                 '$schema': 'http://json-schema.org/draft-07/schema#',
                 'properties': {'a': {'oneOf': [{'description': 'Attributes block SAID',
                                                 'type': 'string'},
                                                {'$id': 'ECDP2TBvNIkBxXViU6_7m4iJdRv-xT5z5R1otJNtfh9O',
                                                 'description': 'Attributes block'}]},
                                'e': {'oneOf': [{'description': 'Edges block SAID',
                                                 'type': 'string'},
                                                {'$id': 'EFNYcwsAkahebjDklBPNRf9dtPbwknx3FxVMxxHRus2g',
                                                 'description': 'Edges block'}]},
                                'r': {'oneOf': [{'description': 'Rules block SAID',
                                                 'type': 'string'},
                                                {'$id': 'EJgcgA00l25ILjwRH6yXYSpAWuomebYMXbNlqNP1HJja',
                                                 'description': 'Rules block'}]}},
                 'type': 'object'}
