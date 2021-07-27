
import time
from typing import Callable


def measure_performance(fn: Callable):
    """
    Decorator to measure time elapsed from Function execution to termination
    """
    def inner(*args, **kwargs):
        start = time.time()
        response = fn(*args, **kwargs)
        end = time.time()
        print(end - start)
        return response
    return inner
