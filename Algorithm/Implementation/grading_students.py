#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            mod = grades[i] % 5
            multi5 = int(((grades[i] - mod) / 5 + 1) * 5)
            if multi5 - grades[i] < 3:
                grades[i] = multi5
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))