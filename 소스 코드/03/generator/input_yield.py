###################################
# File Name : input_yield.py
###################################
#!/usr/bin/python3

def gen():
    value = 2

    while True:
        print (value)
        value = yield

def main():
    print ("=== print gen function ===")
    g = gen()

    next(g)
    g.send(3)
    g.send(5)


if __name__ == "__main__":
    main()
