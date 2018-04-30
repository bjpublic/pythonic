###################################
# File Name : calculator_2.py
###################################
#!/usr/bin/python3

def calculator(x):

    def add(y):
        return x+y

    return add


if __name__ == "__main__":
    print ("=== print calculation ===")
    f = calculator(10)
    print (f(5))
    print (f(10))
