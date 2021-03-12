import pytest
from task01 import count_non_ascii_chars


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", 9), ("data_test01_2.txt", 11)],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    assert count_non_ascii_chars(file_path) == expected_result
