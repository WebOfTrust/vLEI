from vlei.app import generating


def test_schema_said():
    d = \
        {
            "$id": "",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
        }
    d = generating.populateSAIDS(d)

    assert d == {'$id': 'ENAu6EMlVRvJVaDs5b41UXBMqhVYaOLEcPxm6y80Ids8',
                 '$schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object'}


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

    assert d == {'$id': 'EVMnigMh8Dm4v4U9poQyDGXdZ45COiCZPQSKBUhGHCRk',
                 '$schema': 'http://json-schema.org/draft-07/schema#',
                 'properties': {'a': {'$id': 'EZ82qaWXwgkt3Mf-xAi3t9T6kZOOZxzSDSmKTmr6lGig',
                                      'description': 'a'},
                                'e': {'$id': 'EYHM8N5S4InI9fOD_5dyAb2DryUtkIEGFs6w2Iona3qY',
                                      'description': 'e'},
                                'r': {'$id': 'EKoVDEOLuGbrvc2K-9T_Ek29PXDmwz_L_scTWMmULEj4',
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

    assert d == {'$id': 'EMP2q02zKzoNRxH-LDXN2F5gtstN4EcGKEDACRiaPGx0',
                 '$schema': 'http://json-schema.org/draft-07/schema#',
                 'properties': {'a': {'oneOf': [{'description': 'Attributes block SAID',
                                                 'type': 'string'},
                                                {'$id': 'EIM_ZMG80iQHFdWJTr_ubiIl1G_7FPnPlHWi0k21-H04',
                                                 'description': 'Attributes block'}]},
                                'e': {'oneOf': [{'description': 'Edges block SAID',
                                                 'type': 'string'},
                                                {'$id': 'EU1hzCwCRqF5uMOSUE81F_1209vCSfHcXFUzHEdG6zaA',
                                                 'description': 'Edges block'}]},
                                'r': {'oneOf': [{'description': 'Rules block SAID',
                                                 'type': 'string'},
                                                {'$id': 'EmByADTSXbkguPBEfrJdhKkBa6iZ5tgxds2Wo0_UcmNo',
                                                 'description': 'Rules block'}]}},
                 'type': 'object'}
