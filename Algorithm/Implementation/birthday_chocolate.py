#!/bin/python3

import sys


def solve(n, s, d, m):
    # Complete this function
    if m == 1:
        return len([si for si in s if si == d])

    num = 0
    for i in range(0, len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            num += 1
    return num


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
