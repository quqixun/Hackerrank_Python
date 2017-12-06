#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = -1
    for a in range(1, n // 2):
        p1 = (n - a) / 2
        p2 = (a ** 2) / (2 * (n - a))
        b = p1 - p2
        c = p1 + p2
        if int(b) == b and int(c) == c:
            product = int(a * b * c)
            if product > res:
                res = product
    print(res)
