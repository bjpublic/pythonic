###################################
# File Name : compare_none.py
###################################
#!/usr/bin/python3

import timeit

def average(items):
    sum = 0
    for item in items:
        sum += float(item)

    return sum / len(items)

def check_performance(compare_expression, condition):
    results = timeit.Timer(compare_expression, setup=condition).repeat(100, 10000)
    return average(results)

def main():
    print ("=== compare x is not None ===")
    print ("identity : %s" % check_performance("x is None", "x = 1"))
    print ("equality : %s" % check_performance("x == None", "x = 1"))

    print ("=== compare x is None ===")
    print ("identity : %s" % check_performance("x is None", "x = None"))
    print ("equality : %s" % check_performance("x == None", "x = None"))


if __name__ == "__main__":
    main()
