#!/bin/python3

import sys
from bisect import bisect_right

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    # Write Your Code Here
    scores = sorted(set(scores))
    for alice_score in alice:
        print(len(scores) - bisect_right(scores, alice_score) + 1)
