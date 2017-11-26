#!/bin/python3

import sys

def solve(year):
    # Complete this function
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year == 1918:
        days_in_months[1] = 15
    elif year >= 1700 and year <= 1917:
        if year % 4 == 0:
            days_in_months[1] = 29
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_in_months[1] = 29
    
    days_num, day, month = 0, 0, 0
    for i in range(len(days_in_months)):
        days_num += days_in_months[i]
        if days_num > 256:
            month = i + 1
            break
    
    day = 256 - sum(days_in_months[:month - 1])
    
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    year_str = str(year)
    
    return ".".join([day_str, month_str, year_str])

year = int(input().strip())
result = solve(year)
print(result)