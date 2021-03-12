import pytest
from task01 import get_rarest_char


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", "U"), ("data_test01_2.txt", "z")],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    assert get_rarest_char(file_path) == expected_result
