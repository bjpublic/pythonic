###################################
# File Name : closure_cell_attributes.py
###################################
#!/usr/bin/python3

def closure():
    x = 10
    y = 20

    def inner():
        z = 20
        return x+y+z

    return inner


if __name__ == "__main__":
    p = closure()

    print ("=== attribute closure ===")
    print (len(p.__closure__))
    print (p.__closure__[0].cell_contents)
    print (p.__closure__[1].cell_contents)
