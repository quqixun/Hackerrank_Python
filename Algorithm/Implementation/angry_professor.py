#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    arrived_students = 0
    for at in a:
        if at <= 0:
            arrived_students += 1
    if arrived_students < k:
        print("YES")
    else:
        print("NO")
