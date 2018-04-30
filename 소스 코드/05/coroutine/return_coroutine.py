###################################
# File Name : return_coroutine.py
###################################
#!/usr/bin/python3


def return_one_to_ten():
    for i in range(10):
        yield i

def get_coroutine():
    yield return_one_to_ten()

def main():
    print ("== Get coroutine ==")
    c = get_coroutine()
    print (c)

    print ("== Get coroutine's return value ==")
    ret = next(c)
    print(ret)

    print ("== Get values ==")
    print (next(ret))
    print (list(ret))


if __name__ == "__main__":
    main()
