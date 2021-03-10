import hashlib
import random
import struct
import time
from collections.abc import Callable
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(func: Callable = slow_calculate) -> int:
    if __name__ == "__main__":
        pool = Pool(50)
        result = pool.map(func, range(501))
        return sum(result)
