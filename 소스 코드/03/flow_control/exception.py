###################################
# File Name : exception.py
###################################
#!/usr/bin/python3

EXIST_FILE="sample_file"
NON_EXIST_FILE="non_exist_sample_file"

def read_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        print ("File open error")
    else:
        print (f.read())
        f.close()
    finally:
        print ("End file read\n\n")


if __name__ == "__main__":
    print ("=== Exist file open ===")
    read_file(EXIST_FILE)

    print ("=== Non-Exists file open ===")
    read_file(NON_EXIST_FILE)
