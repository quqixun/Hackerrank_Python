#!/bin/python3

import sys


def timeConversion(s):
    # Complete this function
    m = s[-2:]
    h = int(s[0:2])
    if m == "PM":
        if h != 12:
            h += 12
    elif m == "AM":
        if h == 12:
            h = 0
    h = str(h).zfill(2)
    result = h + s[2:-2]
    return result


s = input().strip()
result = timeConversion(s)
print(result)
