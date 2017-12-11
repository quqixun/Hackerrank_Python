#!/bin/python3

import sys
import re


N = int(input().strip())
names = []
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    matchobj = re.search("@gmail.com", emailID)
    if matchobj is not None:
        names.append(firstName)
names.sort()
for n in names:
    print(n)
