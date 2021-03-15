from io import StringIO

import pytest
from task01.task01 import cache


@cache(times=2)
def f():
    return input("? ")


def test_cache_decorator_with_monkeypatch(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", StringIO("1"))
        output_1 = f()
        output_2 = f()
        output_3 = f()
        output_4 = f()

        assert output_1 == output_2 == output_3 != output_4
