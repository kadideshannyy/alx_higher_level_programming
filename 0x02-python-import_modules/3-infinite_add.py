#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for stri in range(len(sys.argv)):
        if (stri == 0):
            continue
        else:
            res += int(sys.argv[stri])
    print("{}".format(res))