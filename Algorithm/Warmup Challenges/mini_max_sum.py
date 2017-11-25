#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
min_value = min(arr)
max_value = max(arr)
sum_arr = sum(arr)

print(sum_arr - max_value, sum_arr - min_value)