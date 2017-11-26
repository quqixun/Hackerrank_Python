#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    birds_num = [0] * 5
    for i in ar:
        birds_num[i - 1] += 1
    return birds_num.index(max(birds_num)) + 1
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)