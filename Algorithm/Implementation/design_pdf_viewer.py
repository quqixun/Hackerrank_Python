#!/bin/python3

import sys
import string


h = list(map(int, input().strip().split(' ')))
word = input().strip()
word_len = len(word)
max_height = 0
for letter in word:
    letter_height = h[string.ascii_lowercase.index(letter)]
    if letter_height > max_height:
        max_height = letter_height
print(word_len * max_height)
