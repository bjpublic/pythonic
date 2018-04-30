###################################
# File Name : iterator.py
###################################
#!/usr/bin/python3

def main():
    x = [1, 2, 3]
    x_iterator = iter(x)

    print ("=== print iterator ===")
    print (next(x_iterator))
    print (next(x_iterator))
    print (next(x_iterator))
    print (next(x_iterator))


if __name__ == "__main__":
    main()
