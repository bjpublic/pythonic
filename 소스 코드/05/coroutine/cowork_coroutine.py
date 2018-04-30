###################################
# File Name : cowork_coroutine.py
###################################
#!/usr/bin/python3

import time
import random

TOTAL_WORK_LOAD = 50

def worker():
    total_work_load = 0
    worker_name = ""

    while True:
        worker_name, total_work_load = yield (worker_name, total_work_load)

        work_load = random.randrange(1, 10)
        work_load = work_load if total_work_load >= work_load else total_work_load
        total_work_load -= work_load

        print ("[%s] Total : %s, work : %s" % (worker_name, total_work_load, work_load))
        yield total_work_load

def main():
    w1 = worker()
    w2 = worker()

    ret = TOTAL_WORK_LOAD
    while ret > 0:
        next(w1)
        ret = w1.send(("w1", ret))

        next(w2)
        ret = w2.send(("w2", ret))


if __name__ == "__main__":
    main()
