#!/bin/python3

import sys


def bubble_sort(a):
    a_len = len(a)
    all_num_swaps = 0
    for i in range(a_len):
        num_swaps = 0
        for j in range(a_len - 1):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp
                num_swaps += 1
                all_num_swaps += 1
        if num_swaps == 0:
            break
    return a, all_num_swaps


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
a, swaps = bubble_sort(a)

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {0}\nLast Element: {1}".format(a[0], a[-1]))