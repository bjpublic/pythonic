###################################
# File Name : unroll_decorator_basic_1.py
###################################
#!/usr/bin/python3

def deco(func):

    def wrapper():
        print ("before")
        ret = func()
        print ("after")
        return ret

    return wrapper

def base():
    print ("base function")


if __name__ == "__main__":
    print ("=== Run decorator ===")
    deco(base)()
