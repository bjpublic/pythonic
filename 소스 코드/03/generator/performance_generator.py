###################################
# File Name : performance_generator.py
###################################
#!/usr/bin/python3

import os
import time
import psutil

def negative_correction(value):
    return 0 if value <= 0 else value

def performance_check(f):
    process = psutil.Process(os.getpid())

    def inner(*args, **kwargs):
        before_mem = process.memory_info().rss / 1024 / 1024
        before_cpu = process.cpu_percent(interval=None)

        t1 = time.clock()
        ret = f(*args, **kwargs)
        t2 = time.clock()

        after_mem = process.memory_info().rss / 1024 / 1024
        after_cpu = process.cpu_percent(interval=None)
        runtime = (t2 - t1)

        cpu = negative_correction(after_cpu - before_cpu)
        mem = negative_correction(after_mem - before_mem)

        return (cpu, mem, runtime)
    return inner

@performance_check
def sum(items):
    ret = 0
    for i in items:
        ret = ("%s%s" % (ret, i))
    return ret

def generator(loop_count):
    result = []
    for i in range(loop_count):
        result.append(i)
    yield result

def summary(count):
    cpu, mem, runtime = 0, 0, 0

    for i in range(count):
        items = generator(100000)
        cpu, mem, runtime = sum(items)
    return (cpu / count, mem / count, runtime / count)


if __name__ == "__main__":
    cpu, mem, runtime = summary(10)
    print ("[CPU Usage] %s" % cpu)
    print ("[Memory Usage] %s" % mem)
    print ("[Runing Time] %s" % runtime)
