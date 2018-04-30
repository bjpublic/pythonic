###################################
# File Name : comprehension.py
###################################
#!/usr/bin/python3

v_list = [1, 2, 3]
v_dict_key = ["korea", "japen", "china"]
v_dict_value = [82, 81, 86]


def print_list_with_comprehension():
    v_list_comprehension = [x*x for x in v_list]
    print (v_list_comprehension)

def print_list_with_for():
    result = []
    for v in v_list:
        result.append(v*v)
    print (result)

def print_dict_with_comprehension():
    v_dict_comprehension = {k:v for k, v in zip(v_dict_key, v_dict_value)}
    print (v_dict_comprehension)


def print_dict_with_for():
    result = {}
    for k, v in zip(v_dict_key, v_dict_value):
        result[k] = v
    print (result)

def main():
    print ("=== print list ===")
    print (v_list)
    print_list_with_comprehension()
    print_list_with_for()

    print ("=== print dict ===")
    print (v_dict_key)
    print (v_dict_value)
    print_dict_with_comprehension()
    print_dict_with_for()


if __name__ == "__main__":
    main()
