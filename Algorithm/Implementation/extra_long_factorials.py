#!/bin/python3

import sys


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input().strip())
print(factorial(n))
