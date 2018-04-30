###################################
# File Name : basic_gevent.py (gevent module)
###################################
#!/usr/bin/python3

import random
import gevent

def worker(index):
    print ("[%s] Enter the work function" % index)
    gevent.sleep(random.randrange(1, 5))
    print ("[%s] Exit the work function" % index)


if __name__ == "__main__":
    workers = [gevent.spawn(worker, i) for i in range(10)]
    gevent.joinall(workers)
