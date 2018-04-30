###################################
# File Name : process_exit.py
###################################
#!/usr/bin/python3

import sys
import time
import multiprocessing


def good_job():
    p = multiprocessing.current_process()
    print ("Start name:%s, pid:%s" % (p.name, p.pid))
    time.sleep(5)
    print ("Exit name:%s, pid:%s" % (p.name, p.pid))
    return 0

def fail_job():
    p = multiprocessing.current_process()
    print ("Start name:%s, pid:%s" % (p.name, p.pid))
    time.sleep(5)
    print ("Exit name:%s, pid:%s" % (p.name, p.pid))
    sys.exit(1)

def kill_job():
    p = multiprocessing.current_process()
    print ("Start name:%s, pid:%s" % (p.name, p.pid))
    time.sleep(10)
    print ("Exit name:%s, pid:%s" % (p.name, p.pid))
    return 0

def main():
    process_list = []
    for func in [good_job, fail_job, kill_job]:
        p = multiprocessing.Process(name=func.__name__, target=func)
        process_list.append(p)

        print ("Process check : %s, %s" % (p, p.is_alive()))
        p.start()
        time.sleep(0.3)

    for p in process_list:
        print ("Process check : %s, %s" % (p, p.is_alive()))

    time.sleep(6)

    for p in process_list:
        print ("Process check : %s, %s" % (p, p.is_alive()))

        if p.is_alive():
            print ("Terminate process : %s" % p)
            p.terminate()

    for p in process_list:
        print ("Process name : %s, exit code : %s" % (p.name, p.exitcode))


if __name__ == "__main__":
    main()
