#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hourglass_sum_list = []
for i in range(4):
    for j in range(4):
        one_sum = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
        hourglass_sum_list.append(one_sum)

print(max(hourglass_sum_list))