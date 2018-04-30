###################################
# File Name : process_queue.py
###################################
#!/usr/bin/python3

import time
import multiprocessing


def set_data(q):
    p = multiprocessing.current_process()
    msg = "Hello World"
    q.put(msg)
    print ("[%s] set queue data : %s" % (p.name, msg))

def get_data(q):
    time.sleep(1)
    p = multiprocessing.current_process()
    print ("[%s] get queue data : %s" % (p.name, q.get()))

def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(name="set_data", target=set_data, args=(queue,))
    p1.start()

    p2 = multiprocessing.Process(name="get_data", target=get_data, args=(queue,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
