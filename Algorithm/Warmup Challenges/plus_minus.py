#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos_num, zero_num, neg_num = 0, 0, 0
for a in arr:
    if a > 0:
        pos_num += 1
    elif a < 0:
        neg_num += 1
    else:
        zero_num += 1

print(pos_num / n)
print(neg_num / n)
print(zero_num / n)
