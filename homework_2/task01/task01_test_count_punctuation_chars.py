import pytest
from task01 import count_punctuation_chars


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", 14), ("data_test01_2.txt", 9)],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    assert count_punctuation_chars(file_path) == expected_result
