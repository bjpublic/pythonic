###################################
# File Name : variable_write_example.py
###################################
#!/usr/bin/python3

msg = "Hello"

def write():
    msg = " World"
    print (msg)

def main():
    print ("=== print msg ===")
    print (msg)

    print ("=== write function ===")
    write()

    print ("=== print msg ===")
    print (msg)


if __name__ == "__main__":
    main()
