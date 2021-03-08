from typing import List, Tuple

import pytest
from task02 import major_and_minor_elem


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, -1, 1, 1, 2, 2], (2, -1)), ([1, 5, 5, 5], (5, 1))],
)
def test_major_and_minor_elem(inp: List, expected_result: Tuple[int, int]):

    assert major_and_minor_elem(inp) == expected_result
