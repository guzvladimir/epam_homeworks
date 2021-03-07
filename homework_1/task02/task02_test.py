from typing import Sequence

import pytest
from task02 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13, 21], True),
        ([0, 1], False),
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], True),
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 97, 144, 241, 377, 610], False),
    ],
)
def test_is_fibonacci(data: Sequence[int], expected_result: bool):

    assert check_fibonacci(data) == expected_result
