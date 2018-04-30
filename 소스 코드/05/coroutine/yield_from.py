###################################
# File Name : yield_from.py (Python 3.3 or later)
###################################
#!/usr/bin/python3


def return_one_to_ten():
    for i in range(10):
        yield i

def get_coroutine():
    yield from return_one_to_ten()

def main():
    print ("== Get coroutine ==")
    c = get_coroutine()
    print (c)

    print ("== Get values ==")
    print (next(c))
    print (list(c))


if __name__ == "__main__":
    main()
