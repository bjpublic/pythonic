###################################
# File Name : upper_case.py
###################################
#!/usr/bin/python3

LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []

def convert():
    for data in LOWER_LIST:
        UPPER_LIST.append(data.upper())

def main():
    print ("=== print result ===")
    convert()
    print (LOWER_LIST)
    print (UPPER_LIST)


if __name__ == "__main__":
    main()
