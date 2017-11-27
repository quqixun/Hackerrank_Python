#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    max_price = 0
    for k in keyboards:
        for d in drives:
            if k + d > max_price and k + d <= s:
                max_price = k + d
    return max_price if max_price > 0 else -1
            

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)