#!/bin/python3

import sys


def simpleArraySum(n, ar):
    # Complete this function
    result = 0
    for i in range(n):
        result += ar[i]
    return result


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
