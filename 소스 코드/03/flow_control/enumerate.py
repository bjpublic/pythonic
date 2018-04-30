###################################
# File Name : enumerate.py
###################################
#!/usr/bin/python3

ALPHABET_LIST = ["a", "b", "c", "d", "e", "f"]

def get_index_basic_method():
    i = 0
    for ch in ALPHABET_LIST:
        print ("%d : %s" % (i, ch))
        i += 1

def get_index_enumerate_method():
    for i, ch in enumerate(ALPHABET_LIST):
        print ("%d : %s" % (i, ch))


if __name__ == "__main__":
    print ("=== Basic method ===")
    get_index_basic_method()

    print ("=== Enumerate method ===")
    get_index_enumerate_method()
