###################################
# File Name : decorator_basic.py
###################################
#!/usr/bin/python3

def deco(func):

    def wrapper():
        print ("before")
        ret = func()
        print ("after")
        return ret

    return wrapper

@deco
def base():
    print ("base function")


if __name__ == "__main__":
    print ("=== Run decorator ===")
    base()
