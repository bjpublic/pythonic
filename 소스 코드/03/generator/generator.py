###################################
# File Name : generator.py
###################################
#!/usr/bin/python3

def gen(items):
    count = 0

    for item in items:
        if count == 10:
            return -1

        count += 1
        yield item


if __name__ == "__main__":
    print ("=== print gen ===")
    for i in gen(range(15)):
        print (i)
