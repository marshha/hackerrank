#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a = [a0, a1, a2]
b = [b0, b1, b2]

a_out = 0
b_out = 0

for a_score in a:
    b_score = b.pop(0)
    if (a_score > b_score):
        a_out += 1
    elif (b_score > a_score):
        b_out += 1

print "%s %s" % (a_out, b_out)
