import time

from task02.task02 import fast_calculate


def test_calculate_how_fast_is_function(max_time: int = 60):
    start_time = time.time()
    fast_calculate()
    end_time = time.time()
    assert end_time - start_time < max_time
