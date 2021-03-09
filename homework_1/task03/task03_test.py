from typing import Tuple

import pytest
from task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [("some_file_1.txt", (1, 5)), ("some_file_2.txt", (11, 58))],
)
def test_is_fibonacci(file_name: str, expected_result: Tuple[int, int]):

    assert find_maximum_and_minimum(file_name) == expected_result
