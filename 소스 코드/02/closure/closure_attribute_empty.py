###################################
# File Name : closure_attribute_empty.py
###################################
#!/usr/bin/python3

def closure():

    def inner():
        pass

    return inner


if __name__ == "__main__":
    p = closure()

    print ("=== attribute closure ===")
    print (p.__closure__)
