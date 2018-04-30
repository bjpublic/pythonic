###################################
# File Name : process_shared_memory.py
###################################
#!/usr/bin/python3

import multiprocessing


def worker(num, num_list):
    p = multiprocessing.current_process()
    print ("[%s] num : %s" % (p.name, num.value))
    for idx, value in enumerate(num_list):
        print ("[%s] num list[%s] : %s" % (p.name, idx, value))

    num.value = 50
    for i in range(len(num_list)):
        num_list[i] = num_list[i] * 10

def main():
    single_integer = multiprocessing.Value("i", 5)
    integer_list = multiprocessing.Array("i", range(10))

    p = multiprocessing.Process(name="worker", target=worker, args=(single_integer, integer_list))
    p.start()

    p.join()
    print ("num : %s" % (single_integer.value))
    for idx, value in enumerate(integer_list):
        print ("num list[%s] : %s" % (idx, value))


if __name__ == "__main__":
    main()
