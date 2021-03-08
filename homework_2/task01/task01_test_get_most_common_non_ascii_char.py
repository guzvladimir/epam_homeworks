import pytest
from task01 import get_most_common_non_ascii_char


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", "ä"), ("data_test01_2.txt", "Ü")],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    assert get_most_common_non_ascii_char(file_path) == expected_result
