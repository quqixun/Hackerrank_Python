#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    if n == 0:
        print(1)
    else:
        for cycle in range(1, n + 1):
            if cycle % 2 == 0:
                height += 1
            else:
                height *= 2
        print(height)
