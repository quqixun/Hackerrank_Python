#!/bin/python3

import sys


n, k, q = input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

l = k % n
a = a[n - l:] + a[:n - l] if l != 0 else a
for a0 in range(q):
    m = int(input().strip())
    print(a[m])
