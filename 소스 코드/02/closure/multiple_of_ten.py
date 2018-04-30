###################################
# File Name : multiple_of_ten.py
###################################
#!/usr/bin/python3

def multiple_of_ten():
    square_root = 10

    def square(x):
        return square_root ** x

    return square

def main():
    print ("=== print result ===")
    f = multiple_of_ten()

    print (f(2))
    print (f(3))


if __name__ == "__main__":
    main()
