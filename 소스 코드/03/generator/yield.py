###################################
# File Name : yield.py
###################################
#!/usr/bin/python3

def gen():
    value = 1
    while True:
        value = yield value

def main():
    print ("=== print gen function ===")
    g = gen()

    print (next(g))
    print (g.send(2))
    print (g.send(10))
    print (g.send(5))
    print (next(g))


if __name__ == "__main__":
    main()
