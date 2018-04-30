###################################
# File Name : partial_application_with_closure.py
###################################
#!/usr/bin/python3

def partial(func, *partial_args):

    def wrapper(*extra_args):
        args = list(partial_args)
        args.extend(extra_args)

        return func(*args)
    return wrapper

def logging(year, month, day, title, content):
    print ("%s-%s-%s %s:%s" % (year, month, day, title, content))

def main():
    print ("=== use logging function ===")
    logging("2017", "12", "28", "python2", "End of support in 2020")
    logging("2017", "12", "28", "python3", "Updating")


    print ("=== use partial function ===")
    f = partial(logging, "2017", "12", "28")
    f("python2", "End of support in 2020")
    f("python3", "Updating")


if __name__ == "__main__":
    main()
