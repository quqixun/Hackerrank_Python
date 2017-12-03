#!/bin/python3

import sys


def isPalindrome(n):
    nStr = str(n)
    return nStr == nStr[::-1]


def getMaxPalindrome(n):
    max_pal = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            mul = i * j
            if mul >= n:
                continue
            if mul <= max_pal:
                break
            if isPalindrome(mul):
                max_pal = mul
    return max_pal


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(getMaxPalindrome(n))
