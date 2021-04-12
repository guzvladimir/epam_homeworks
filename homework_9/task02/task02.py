"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager
from types import TracebackType
from typing import Iterator, Optional, Type


class SuppressorClass:
    def __init__(self, exception: Optional[Type[BaseException]]):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[Type[TracebackType]],
    ):
        return exception_type is not None and isinstance(
            exception_value, self.exception
        )


@contextmanager
def suppressor(exception: Optional[Type[BaseException]]) -> Iterator:
    try:
        yield
    except exception:
        pass
