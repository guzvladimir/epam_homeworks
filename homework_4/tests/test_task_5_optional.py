import types
from typing import List

import pytest
from task05.task_5_optional import fizzbuzz


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (5, ["1", "2", "fizz", "4", "buzz"]),
        (0, []),
        (
            15,
            [
                "1",
                "2",
                "fizz",
                "4",
                "buzz",
                "fizz",
                "7",
                "8",
                "fizz",
                "buzz",
                "11",
                "fizz",
                "13",
                "14",
                "fizzbuzz",
            ],
        ),
    ],
)
def test_fizzbuzz(value: int, expected_result: List[str]):
    actual_result = list(fizzbuzz(value))
    assert actual_result == expected_result


def test_fizzbuzz_is_generator():
    actual_result = fizzbuzz(5)
    assert isinstance(actual_result, types.GeneratorType)


def test_fizzbuzz_gen():
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]
