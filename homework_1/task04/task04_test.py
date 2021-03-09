from typing import List

import pytest
from task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        (
            [5, -2, 0, 4, -5],
            [6, 1, 3, 9, 5],
            [-1, 12, -3, 7, 5],
            [16, -8, 15, -8, 20],
            18,
        ),
        ([4, 6, 0, 4], [6, 9, 3, -5], [-13, 12, 3, 7], [6, -8, 15, -4], 4),
    ],
)
def test_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):

    assert check_sum_of_four(a, b, c, d) == expected_result
