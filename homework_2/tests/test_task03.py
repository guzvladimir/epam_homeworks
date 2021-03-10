from typing import Any, List

import pytest
from task03.task03 import combinations


@pytest.mark.parametrize(
    ["values", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (([5, 6], [7, 8]), [[5, 7], [5, 8], [6, 7], [6, 8]]),
        (
            ([1, 2], [3, 4], [5, 6]),
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        ),
    ],
)
def test_combinations(values: List[Any], expected_result: List[List]):

    assert combinations(*values) == expected_result
