#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

step = 0
pos = 0
while pos != (n - 1):
    step += 1
    if pos == (n - 3) or pos == (n - 2):
        pos = n - 1
    else:
        if c[pos + 2] != 1:
            pos += 2
        else:
            pos += 1
print(step)
