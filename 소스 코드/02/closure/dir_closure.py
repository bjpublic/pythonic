###################################
# File Name : dir_closure.py
###################################
#!/usr/bin/python3

def closure():

    def inner():
        pass

    p = dir(inner())

    print ("=== inner attribute ===")
    print (p)
    return inner


if __name__ == "__main__":
    p = dir(closure())

    print ("=== attribute ===")
    print (p)
