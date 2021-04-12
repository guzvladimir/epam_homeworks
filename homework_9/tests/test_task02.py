from task02.task02 import SuppressorClass, suppressor


def test_suppressor_class_index_error():
    with SuppressorClass(IndexError):
        assert [1, 2][3]


def test_suppressor_generator_value_error():
    with suppressor(ValueError):
        assert int("string")


def test_suppressor_class_and_generator_zero_division_error():
    with SuppressorClass(ZeroDivisionError):
        assert 13 / 0
    with suppressor(ZeroDivisionError):
        assert 12 / 0
