###################################
# File Name : expression.py
###################################
#!/usr/bin/python3

SAMPLE_LIST = [1, 2, 3, 4, 5]

def generate_sample_list():
    result = (x*x for x in SAMPLE_LIST)
    print (result)
    return result

def generate_list_by_range():
    result = (i for i in range(10))
    print (result)
    return result

def print_generator(items):
    for item in items:
        print (item)

def main():
    print ("=== print list ===")
    print_generator(generate_sample_list())
    print_generator(generate_list_by_range())


if __name__ == "__main__":
    main()
