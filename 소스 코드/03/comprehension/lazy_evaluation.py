###################################
# File Name : lazy_evaluation.py
###################################
#!/usr/bin/python3

import time

def wait_return(num):
    print ("sleep")
    time.sleep(0.5)
    return num

def print_items(items):
    for i in items:
        print (i)

def main():
    print ("=== print list comprehension ===")
    iterator_list = [wait_return(i) for i in range(10)]
    print_items(iterator_list)

    print ("=== print generator expression ===")
    iterator_list = (wait_return(i) for i in range(10))
    print_items(iterator_list)


if __name__ == "__main__":
    main()
