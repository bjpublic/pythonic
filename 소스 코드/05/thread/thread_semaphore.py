###################################
# File Name : thread_semaphore.py
###################################
#!/usr/bin/python3

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")


class ResourcePool():

    def __init__(self):
        self.active_thread_list = []
        self.lock = threading.Lock()

    def use(self, name):
        with self.lock:
            self.active_thread_list.append(name)
            logging.debug("List of threads in resource pool : %s", self.active_thread_list)

    def unuse(self, name):
        with self.lock:
            self.active_thread_list.remove(name)
            logging.debug("List of threads in resource pool : %s", self.active_thread_list)


def worker(semaphore, pool):
    logging.debug("Waiting to enter the pool.")
    with semaphore:
        logging.debug("Enter the pool.")
        thread_name = threading.currentThread().getName()
        pool.use(thread_name)
        time.sleep(1)
        pool.unuse(thread_name)

def main():
    pool = ResourcePool()
    semaphore = threading.Semaphore(3)

    for i in range(5):
        t = threading.Thread(target=worker, name=("thread-%s" % i), args=(semaphore, pool))
        t.start()


if __name__ == "__main__":
    main()
