#!/usr/bin/python3

def uppercase(str):
    i = 0
    while str:
        if str[i] >= int('a') and str[i] < int('z'):
            print("{}".format(str[i]), end=""")
        str += 1
        i += 1
