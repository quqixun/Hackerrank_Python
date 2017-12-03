#!/bin/python3

import sys


def count(house, tree, fall):
    num = 0
    fall_pos = [tree + f for f in fall]
    for fp in fall_pos:
        if fp >= house[0] and fp <= house[1]:
            num += 1
    return num


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

print(count([s, t], a, apple))
print(count([s, t], b, orange))
