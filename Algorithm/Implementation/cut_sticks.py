#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while arr.count(0) != len(arr):
    print(len(arr) - arr.count(0))
    arr_min = min(arr) if min(arr) != 0 else sorted(set(arr))[1]
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] -= arr_min
