###################################
# File Name : arguments.py
###################################
#!/usr/bin/python3

def test(name, *args, **kwargs):
    print ("=== fixed argument ===")
    print ("Fixed argument : %s" % name)

    print ("=== args list ===")
    for arg in args:
        print ("Argument : %s" % arg)

    print ("=== kwargs list ===")
    for keyword, arg in kwargs.items():
        print ("Argument keyword : %s, arg : %s" % (keyword, arg))

def main():
    args = ["red", "blue", "first", "second"]
    kwargs = {"red":"color", "blue":"color", "first":"number", "second":"number"}


    test("python", *args, **kwargs)
    test("python", "red", "blue", "green", red="color", blue="color")


if __name__ == "__main__":
    main()
