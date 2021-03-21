import functools

import pytest
from task02.save_original_info import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_print_result():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum_with_parametrize(value, expected_result):

    assert custom_sum(*value) == expected_result


def test_original_function_executes_without_print():
    without_print = custom_sum.__original_func
    result = without_print(1, 2, 3, 4)

    assert result == 10
