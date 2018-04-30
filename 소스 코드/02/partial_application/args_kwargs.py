###################################
# File Name : args_kwargs.py
###################################
#!/usr/bin/python3

def args_test(*args):
    print ("=== args list ===")
    for arg in args:
        print ("Argument : %s" % arg)

def kwargs_test(**kwargs):
    print ("=== kwargs list ===")
    for keyword, arg in kwargs.items():
        print ("Argument keyword : %s, arg : %s" % (keyword, arg))

def main():
    args = ["red", "blue", "first", "second"]
    kwargs = {"red":"color", "blue":"color", "first":"number", "second":"number"}

    args_test(*args)
    kwargs_test(**kwargs)


if __name__ == "__main__":
    main()
