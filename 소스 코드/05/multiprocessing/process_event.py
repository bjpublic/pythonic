###################################
# File Name : process_event.py
###################################
#!/usr/bin/python3

import time
import multiprocessing


def first_wait(e1, e2):
    p = multiprocessing.current_process()
    while not e1.is_set():
        event = e1.wait(1)
        print ("[%s] Event status : (%s)" % (p.name, event))

        if event:
            print ("[%s] e1 is set." % p.name)
            time.sleep (3)
            print ("[%s] Set e2" % p.name)
            e2.set()

def second_wait(e2):
    p = multiprocessing.current_process()
    while not e2.is_set():
        event = e2.wait(1)
        print ("[%s] Event status : (%s)" % (p.name, event))

        if event:
            print ("[%s] e2 is set." % p.name)

def main():
    e1 = multiprocessing.Event()
    e2 = multiprocessing.Event()

    p1 = multiprocessing.Process(name="first", target=first_wait, args=(e1, e2))
    p1.start()

    p2 = multiprocessing.Process(name="second", target=second_wait, args=(e2,))
    p2.start()


    print ("Wait ...")
    time.sleep(5)
    print ("Set e1")
    e1.set()
    time.sleep(5)
    print ("Exit")


if __name__ == "__main__":
    main()
