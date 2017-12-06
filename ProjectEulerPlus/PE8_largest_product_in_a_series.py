#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    num_str = str(num)
    max_product = 0
    for i in range(0, n - k + 1):
        k_digits = num_str[i:i + k]
        product = 1
        for kd in k_digits:
            if kd == "0":
                product = 0
                break
            else:
                product *= int(kd)
        if product > max_product:
            max_product = product
    print(max_product)
