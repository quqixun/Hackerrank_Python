#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a_set = list(set(a))
max_num = 0
for at in a_set:
    num = a.count(at) + a.count(at - 1)
    if num > max_num:
        max_num = num
print(max_num)
