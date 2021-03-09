from typing import List

import pytest
from task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([3, 5, 16, -1, 6, 4, 1, -5], 4, 26),
        ([1, 1, 1, 3, 0, -5, 10], 2, 5),
        ([0, 1, -1, 2, -3, 4, 9], 3, 10),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):

    assert find_maximal_subarray_sum(nums, k) == expected_result
