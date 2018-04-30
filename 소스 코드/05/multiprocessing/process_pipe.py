###################################
# File Name : process_pipe.py
###################################
#!/usr/bin/python3

import multiprocessing


def child(pipe):
    p = multiprocessing.current_process()

    msg = "Hello World"
    pipe.send(msg)

    print ("[%s] Send a message to pipe : %s" % (p.name, msg))

def main():
    parent_pipe, child_pipe = multiprocessing.Pipe()

    p = multiprocessing.Process(name="child", target=child, args=(child_pipe,))
    p.start()

    print ("Recieved message : %s" % parent_pipe.recv())
    p.join()


if __name__ == "__main__":
    main()
