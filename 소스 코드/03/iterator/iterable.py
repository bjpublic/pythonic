###################################
# File Name : iterable.py
###################################
#!/usr/bin/python3

def main():
    x = [1, 2, 3]
    y = {"red":1, "blue":2, "green":3}

    x_iterator = iter(x)
    y_iterator = iter(y)

    print ("=== print type ===")
    print ("list type : %s" % type(x))
    print ("dictonary type : %s" % type(y))
    print ("list iterator type : %s" % type(x_iterator))
    print ("dictonary iterator type : %s" % type(y_iterator))

    print ("=== print next ===")
    print ("list iterator next : %s" % next(x_iterator))
    print ("dictionary iterator next : %s" % next(y_iterator))
    print ("list next : %s" % next(x))
    print ("dictionary next : %s" % next(y))


if __name__ == "__main__":
    main()
