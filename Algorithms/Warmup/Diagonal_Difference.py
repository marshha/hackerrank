#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum_1 = 0
sum_2 = 0
i = 0
for row in a:
    sum_1 += row[i]
    sum_2 += row[(n-1) - i]
    i += 1

print abs(sum_1 - sum_2)
