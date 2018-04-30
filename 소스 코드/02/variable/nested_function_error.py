###################################
# File Name : nested_function_error.py
###################################
#!/usr/bin/python3

def greeting(name):
    greeting_msg = "Hello"

    def add_name():
        greeting_msg += " "
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print (msg)


if __name__ == "__main__":
    greeting("python")
