#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    num = n * (n - 1) if n > 1 else 1
    while(True):
        stop = True
        for i in range(1, n + 1):
            if num % i != 0:
                stop = False
                break
        
        if not stop:
            num += 1
        else:
            print(num)
            break