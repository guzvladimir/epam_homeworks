"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        return exception_type is not None and isinstance(
            exception_value, self.exception
        )


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass
