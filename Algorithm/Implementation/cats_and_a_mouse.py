#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    xz_dis = abs(z - x)
    yz_dis = abs(z - y)
    if xz_dis < yz_dis:
        print("Cat A")
    elif yz_dis < xz_dis:
        print("Cat B")
    else:
        print("Mouse C")