from typing import Any, List

import pytest
from task05 import custom_range


@pytest.mark.parametrize(
    ["iterable_values", "values", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "g", ["a", "b", "c", "d", "e", "f"]),
        (
            "abcdefghijklmnopqrstuvwxyz",
            ("g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ("abcdefghijklmnopqrstuvwxyz", ("p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(iterable_values: str, values: Any, expected_result: List[Any]):
    assert custom_range(iterable_values, *values) == expected_result
