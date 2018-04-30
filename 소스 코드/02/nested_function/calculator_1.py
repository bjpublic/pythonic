###################################
# File Name : calculator_1.py
###################################
#!/usr/bin/python3

def calculator(x, y):

    def add():
        return x+y

    def sub():
        return x-y

    return (add(), sub())


if __name__ == "__main__":
    print ("=== print calculation ===")
    print (calculator(10, 5))
