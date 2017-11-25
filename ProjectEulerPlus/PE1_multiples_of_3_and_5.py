#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    div3 = (n - 1) // 3
    div5 = (n - 1) // 5
    div15 = (n - 1) // 15
    total = div3 * (div3 + 1) * 3 // 2 + \
            div5 * (div5 + 1) * 5 // 2 - \
            div15 * (div15 + 1) * 15 // 2
    print(total)