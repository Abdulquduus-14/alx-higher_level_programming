#!/usr/bin/python3
n = 97

for i in range(26):
    n = n + i
    s = chr(n)
    print("{}".format(s), end="")
