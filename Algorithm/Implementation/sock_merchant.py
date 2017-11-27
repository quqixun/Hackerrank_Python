#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    all_sizes = list(set(ar))
    pairs_num = 0
    
    for s in all_sizes:
        s_num = ar.count(s)
        pairs_num += s_num // 2
    
    return pairs_num
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)