from typing import Any, Callable, Sequence


def cache(times: int) -> Callable:
    def cache_decorator(func: Callable) -> Callable:
        times_counter = 0
        result = None

        def wrapper(*args: Sequence[Any]) -> Any:
            nonlocal times_counter, result
            if times_counter > 0:
                times_counter -= 1

                return result
            else:
                result = func(*args)
                times_counter = times

                return result

        return wrapper

    return cache_decorator
