"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(iterable_values: str, *args: Any) -> List[Any]:
    keys = slice(*args)
    start = 0
    if keys.start:
        start = iterable_values.index(keys.start)
    stop = iterable_values.index(keys.stop)
    step = keys.step or 1
    sequence = iterable_values[start:stop:step]
    result = [letter for letter in sequence]
    return result
