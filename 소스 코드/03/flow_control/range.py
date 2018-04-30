###################################
# File Name : range.py
###################################
#!/usr/bin/python3

import sys

def get_type_and_size(value):
	print ("type : %s" % type(value))
	print ("size : %d" % sys.getsizeof(value))

def main():
    print ("=== Range size : 10 ===")
    get_type_and_size(range(10))

    print ("=== Range size : 100 ===")
    get_type_and_size(range(100))

    print ("=== Xrange size : 10 ===")
    get_type_and_size(xrange(10))


if __name__ == "__main__":
    main()
