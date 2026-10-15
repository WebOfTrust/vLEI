"""The schema server must run on one consistent GLEIF dependency chain."""
from importlib import metadata
import hio
import keri
import vlei


def test_release_dependencies_have_exclusive_import_ownership():
    names = {d.metadata["Name"].lower().replace("_", "-") for d in metadata.distributions()}
    assert not {"keri", "hio"} & names
    assert metadata.version("gleif-hio") == hio.__version__ == "0.6.21"
    assert metadata.version("gleif-keri") == keri.__version__ == "1.2.16"
    assert metadata.version("vlei") == vlei.__version__ == "1.0.4"
