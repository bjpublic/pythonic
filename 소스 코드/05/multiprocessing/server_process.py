###################################
# File Name : server_process.py
###################################
#!/usr/bin/python3

import multiprocessing

def print_array_or_list(name, values):
    for idx, value in enumerate(values):
        print ("[%s] num list[%s] : %s" % (name, idx, value))

def worker(v, a, l, d):
    p = multiprocessing.current_process()
    print ("[%s] value : %s, dict : %s" % (p.name, v, d["key"]))
    print_array_or_list(p.name, a)
    print_array_or_list(p.name, l)

    v.value = 50
    for i in range(len(a)):
        a[i] = a[i] * 10

    for i in range(len(l)):
        l[i] = l[i] * 10

    d["key"] = "Python3"

def main():
    manager = multiprocessing.Manager()

    v = manager.Value("i", 5)
    a = manager.Array("i", range(10))
    l = manager.list(range(10))
    d = manager.dict()
    d["key"] = "Python2"

    p = multiprocessing.Process(name="worker", target=worker, args=(v, a, l, d))
    p.start()

    p.join()
    main_name = "main"
    print ("[%s] value : %s, dict : %s" % (main_name, v, d["key"]))
    print_array_or_list(main_name, a)
    print_array_or_list(main_name, l)


if __name__ == "__main__":
    main()
