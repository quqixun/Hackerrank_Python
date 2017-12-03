#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    plain_sum = (1 + n) * n // 2
    square_sum = n * (n + 1) * (2 * n + 1) // 6
    print(plain_sum ** 2 - square_sum)