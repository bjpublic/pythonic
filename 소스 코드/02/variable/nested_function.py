###################################
# File Name : nested_function.py
###################################
#!/usr/bin/python3

def greeting(name):
    greeting_msg = "Hello "

    def add_name():
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print (msg)


if __name__ == "__main__":
    greeting("python")
