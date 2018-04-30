###################################
# File Name : variable_shadowing.py
###################################
#!/usr/bin/python3

var_shadowing = "global"

def outer_function():
    var_shadowing = "outer"

    def inner_function():
        var_shadowing = "inner"
        print ("inner_function scope: %s" % var_shadowing)

    inner_function()
    print ("outer_function scope: %s" % var_shadowing)


if __name__ == "__main__":
    outer_function()
    print ("global scope: %s" % var_shadowing)
