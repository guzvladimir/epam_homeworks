import pytest
from task04.task04 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(1, True), (153, True), (444, False)],
)
def test_is_armstrong(number: int, expected_result: bool):

    assert is_armstrong(number) == expected_result
