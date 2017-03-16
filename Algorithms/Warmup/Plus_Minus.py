#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zero = 0

for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

tot = pos + neg + zero
print float(pos)/float(tot)
print float(neg)/float(tot)
print float(zero)/float(tot)

