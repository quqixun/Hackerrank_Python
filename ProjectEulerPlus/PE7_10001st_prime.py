#!/bin/python3

import sys


def primes(n, pl):
    p = pl[-1]
    while len(pl) < n:
        p += 2
        pt = int(p ** 0.5)
        for i in pl:
            if i > pt:
                pl.append(p)
                break
            if p % i == 0:
                break
    return pl


t = int(input().strip())
pl = [2, 3]
for a0 in range(t):
    n = int(input().strip())
    if n > len(pl):
        pl = primes(n, pl)
    print(pl[n - 1])
