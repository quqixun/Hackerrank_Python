#!/bin/python3

import sys


class Difference:

    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        diffs_list = []
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                diffs_list.append(abs(self.__elements[i] - self.__elements[j]))
        self.maximumDifference = max(diffs_list)
        return


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
