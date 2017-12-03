#!/bin/python3

import sys

s = []
for s_i in range(3):
    s += [int(s_temp) for s_temp in input().strip().split(' ')]
#  Print the minimum cost of converting 's' into a magic square
all = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
       [6, 1, 8, 7, 5, 3, 2, 9, 4],
       [4, 9, 2, 3, 5, 7, 8, 1, 6],
       [2, 9, 4, 7, 5, 3, 6, 1, 8],
       [8, 3, 4, 1, 5, 9, 6, 7, 2],
       [4, 3, 8, 9, 5, 1, 2, 7, 6],
       [6, 7, 2, 1, 5, 9, 8, 3, 4],
       [2, 7, 6, 9, 5, 1, 4, 3, 8]]

print(min([sum([abs(i - j) for i, j in zip(s, l)]) for l in all]))
