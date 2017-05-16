import os
import inspect
import time
import platform
import multiprocessing as mp

from functools import wraps


def logger(func):
    # to preserve the original function meta data we need to apply wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        pyversion = 'Python-%s' % (platform.python_version())
        # assuming first argument id the cpu/thread count
        count = args[0] if len(args) else 0
        print(
            "%15s[%15s] : %d CPU, %2d Thread/Process, Time %.6f" %
            (pyversion,
             inspect.getmodule(func).__file__,
             mp.cpu_count(),
             count,
             end -
             start))
        return f
    return wrapper
