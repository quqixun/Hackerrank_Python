#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diag1 = [a[i][i] for i in range(n)]
diag2 = [a[i][n-1-i] for i in range(n)]
diag_diff = abs(sum(diag2) - sum(diag1))
print(diag_diff)