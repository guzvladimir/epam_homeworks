from collections.abc import Callable
from typing import Tuple

import pytest
from task04 import cache


@pytest.mark.parametrize(
    ["func", "some", "expected_result"],
    [
        ((lambda a, b: (a ** b) ** 2), (100, 200), True),
        ((lambda a, b, c: a ** b + c), (10, 2, 3), True),
    ],
)
def test_cache(func: Callable, some: Tuple[int], expected_result: bool):
    cache_func = cache(func)
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
