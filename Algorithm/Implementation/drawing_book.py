#!/bin/python3

import sys


def solve(n, p):
    # Complete this function
    begin_to_page = int(p / 2)
    end_to_page = int(n / 2) - begin_to_page
    return min([begin_to_page, end_to_page])


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
