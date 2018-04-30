###################################
# File Name : class_decorator.py
###################################
#!/usr/bin/python3

import time
from functools import update_wrapper

class MeasureRuntime:

    def __init__(self, f):
        self.func = f
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print ("'%s' function running time : %s" % (self.func.__name__, end - start))
        return result


@MeasureRuntime
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
