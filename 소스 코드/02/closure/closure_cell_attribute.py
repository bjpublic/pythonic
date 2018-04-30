###################################
# File Name : closure_cell_attribute.py
###################################
#!/usr/bin/python3

def closure():
    x = 10

    def inner():
        y = 20
        return x+y

    return inner


if __name__ == "__main__":
    p = closure()

    print ("=== attribute closure ===")
    print (len(p.__closure__))
    print (dir(p.__closure__[0]))
