###################################
# File Name : partial_application_with_functools.py
###################################
#!/usr/bin/python3

from functools import partial

def logging(year, month, day, title, content):
    print ("%s-%s-%s %s:%s" % (year, month, day, title, content))

def main():
    print ("=== use partial function ===")
    f = partial(logging, "2017", "12", "28")
    f("python2", "End of support in 2020")
    f("python3", "Updating")


if __name__ == "__main__":
    main()
