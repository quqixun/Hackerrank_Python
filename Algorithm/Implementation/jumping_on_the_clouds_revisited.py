#!/bin/python3

import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

E = 100
for i in range(n // k):
    E -= 1
    if c[i * k] == 1:
        E -= 2
print(E)
