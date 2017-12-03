#!/bin/python3

import sys


n = int(input())

phone_dict = {}
for _ in range(n):
    phone_num_data = input().split(" ")
    phone_dict[phone_num_data[0]] = phone_num_data[1]
phone_dict_keys = phone_dict.keys()

for _ in range(n):
    query = input()
    if query in phone_dict_keys:
        print(query + "=" + phone_dict[query])
    else:
        print("Not found")
