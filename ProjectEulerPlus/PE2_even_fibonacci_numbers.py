#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibo = [1, 2, 3, 5, 8]
    even_fibo = [2, 8]
    next_fibo = 13
    while next_fibo < n:
        fibo.append(next_fibo)
        if next_fibo % 2 == 0:
            even_fibo.append(next_fibo)
        next_fibo = fibo[-1] + fibo[-2]
    print(sum(even_fibo))