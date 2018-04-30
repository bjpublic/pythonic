###################################
# File Name : basic_greenlet.py (greenlet module)
###################################
#!/usr/bin/python3

import greenlet

def worker1():
    print ("Enter the work1 function")
    gr2.switch()
    print ("Exit the work1 function")

def worker2():
    print ("Enter the work2 function")
    gr1.switch()
    print ("Exit the work2 function")


if __name__ == "__main__":
    gr1 = greenlet.greenlet(worker1)
    gr2 = greenlet.greenlet(worker2)
    gr1.switch()
