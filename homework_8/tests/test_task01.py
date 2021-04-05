import pytest
from task01.task01 import KeyValueStorage


def test_keyvaluestorage():
    storage = KeyValueStorage("task1.txt")
    assert storage["name"] == storage.name == "kek"
    assert storage.song == "shadilay"


def test_value_error():
    with pytest.raises(
        ValueError, match="This key cannot be assigned to an attribute."
    ):
        KeyValueStorage("test_task01_negative.txt")
