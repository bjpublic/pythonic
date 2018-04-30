###################################
# File Name : basic_threading_function.py
###################################
#!/usr/bin/python3

import threading

def worker(count):
    print ("name : %s, argument : %s" % (threading.currentThread().getName(), count))

def main():
    for i in range(5):
        t = threading.Thread(target=worker, name="thread %i" % i, args=(i,))
        t.start()


if __name__ == "__main__":
    main()
