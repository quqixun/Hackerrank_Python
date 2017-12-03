#!/bin/python3

import sys


def getTotalX(a, b):
    # Complete this function
    if max(a) > min(b):
        return 0

    if max(a) == min(b):
        return 1

    pb_list = list(range(max(a), min(b) + 1))
    rm_list = []
    for p in pb_list:
        for ta in a:
            if p % ta != 0:
                rm_list.append(p)
                break
    for p in pb_list:
        for tb in b:
            if tb % p != 0:
                rm_list.append(p)
                break
    rm_list = list(set(rm_list))
    return len(pb_list) - len(rm_list)


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
