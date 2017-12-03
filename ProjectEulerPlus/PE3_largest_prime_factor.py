#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    i = 2
    while (i ** 2) <= n:
        if n % i:
            i += 1
        else:
            n //= i

    print(n)
