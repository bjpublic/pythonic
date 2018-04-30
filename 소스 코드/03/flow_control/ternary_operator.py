###################################
# File Name : ternary_operator.py
###################################
#!/usr/bin/python3

def check_boolean(value):
    if type(value) == bool:
        return True
    else:
        return False

def check_boolean_ternary_operator(value):
    return True if type(value) == bool else False

def main():
    print ("=== basic if/else ===")
    print ("Input boolean : %s" % check_boolean(True))
    print ("Input string : %s" % check_boolean("string"))

    print ("=== ternary operator ===")
    print ("Input boolean : %s" % check_boolean_ternary_operator(True))
    print ("Input boolean : %s" % check_boolean_ternary_operator("string"))


if __name__ == "__main__":
    main()
