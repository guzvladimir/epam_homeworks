import os
from pathlib import Path

from task03.task03 import universal_file_counter

path = Path(os.path.dirname(__file__))


def test_universal_file_counter_with_tokenizer_data_split_by_space():
    assert universal_file_counter(path, "txt", str.split) == 11


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter(path, "txt") == 10
