###################################
# File Name : compare_identity.py
###################################
#!/usr/bin/python3

def main():
    print ("=== compare identity ===")
    print (999 is 999)
    x = 999; y = 999;
    print (x is y)
    z = 999;
    print (x is z)


if __name__ == "__main__":
    main()
