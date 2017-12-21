#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

san = s.count("a")
nc = n // len(s)
mc = n % len(s)
lan = s[:mc].count("a")
num = san * nc + lan
print(num)
