#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

ls, lt = len(s), len(t)
lm = min([ls, lt])

cm = 0
for i in range(lm):
    if s[i] == t[i]:
        cm += 1
    else:
        break
diff = ls + lt - 2 * cm
if diff > k:
    print("No")
elif (diff % 2) == (k % 2):
    print("Yes")
elif ls + lt < k:
    print("Yes")
else:
    print("No")
