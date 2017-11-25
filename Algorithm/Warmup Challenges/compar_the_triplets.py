#!/bin/python3

import sys

def score(a, b):
    if a > b:
        return 0
    elif a < b:
        return 1
    else:
        return -1

def add_score(score, result):
    if score != -1:
        result[score] += 1
    return score

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    result = [0, 0]
    score0 = score(a0, b0)
    retult = add_score(score0, result)
    score1 = score(a1, b1)
    retult = add_score(score1, result)
    score2 = score(a2, b2)
    retult = add_score(score2, result)
    return result
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))