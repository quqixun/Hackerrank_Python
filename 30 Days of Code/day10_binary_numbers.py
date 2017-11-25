#!/bin/python3

import sys


n = int(input().strip())

bin_list = []
while(n > 0):
    div_res = n // 2
    mod_res = n % 2
    bin_list.append(mod_res)
    n = div_res
bin_list = list(reversed(bin_list))

bin_one_num_list = []
temp = []
for i in range(len(bin_list)):
    b = bin_list[i]
    if b == 1:
        temp.append(b)
    
    if b == 0 or i == len(bin_list) - 1:
        if len(temp) > 0:
            bin_one_num_list.append(len(temp))
        temp = []
print(max(bin_one_num_list))