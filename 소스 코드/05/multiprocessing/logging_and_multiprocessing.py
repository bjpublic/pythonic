###################################
# File Name : logging_and_multiprocessing.py
###################################
#!/usr/bin/python3

import logging
import multiprocessing

def worker(count):
    print ("count : %s" % count)

def main():
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.DEBUG)

    for i in range(5):
        t = multiprocessing.Process(target=worker, args=(i,))
        t.start()


if __name__ == "__main__":
    main()
