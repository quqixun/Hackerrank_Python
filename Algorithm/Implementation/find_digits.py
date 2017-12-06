#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num = 0
    for c in str(n):
        if c == "0":
            continue
        else:
            if n % int(c) == 0:
                num += 1
    print(num)
