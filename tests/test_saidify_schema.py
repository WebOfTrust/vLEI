import json
from pathlib import Path

import os

import multicommand
import pytest
from keri.core import scheming
import subprocess

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def test_saidify_schema_command():

    filepath = os.path.join(TEST_DIR, "schema-sample.json")
    result = subprocess.run(['saidify-schema', '--file',  filepath, '--schema-dir', TEST_DIR], capture_output=True)
    
    with open(filepath) as f:
        sed = json.load(f)
        schemer = scheming.Schemer(sed=sed)
        assert schemer.said == 'EBfdlu8R27Fbx-ehrqwImnK-8Cm79sqbAQ4MmvEAYqao'        

    