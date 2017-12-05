#!/bin/python3

import sys


def birthdayCakeCandles(n, ar):
    # Complete this function
    max_height = max(ar)
    result = 0
    for a in ar:
        if a == max_height:
            result += 1
    return result


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
