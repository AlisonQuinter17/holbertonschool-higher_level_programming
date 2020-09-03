#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    add = 0
    if num == 0:
        print("0")
    elif num == 1:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, num):
            add = add + int(sys.argv[i])
        print("{}".format(add))
