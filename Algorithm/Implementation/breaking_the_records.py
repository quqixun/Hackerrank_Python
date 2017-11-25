#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    hs, ls = s[0], s[0]
    hnum, lnum = 0, 0
    for si in s[1:]:
        if si > hs:
            hs = si
            hnum += 1
        elif si < ls:
            ls = si
            lnum += 1
        else:
            pass
    return [hnum, lnum]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))