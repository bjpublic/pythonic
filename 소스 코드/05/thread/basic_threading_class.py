###################################
# File Name : basic_threading_class.py
###################################
#!/usr/bin/python3

import threading

class Worker(threading.Thread):

    def __init__(self, args, name=""):
        threading.Thread.__init__(self)
        self.args = args

    def run(self):
        print ("name : %s, argument : %s" % (threading.currentThread().getName(), self.args[0]))


def main():
    for i in range(5):
        t = Worker(name="thread %i" % i, args=(i,))
        t.start()


if __name__ == "__main__":
    main()
