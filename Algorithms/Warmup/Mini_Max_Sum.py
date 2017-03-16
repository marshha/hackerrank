#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
int_vals = [int(a),int(b),int(c),int(d),int(e)]

min = None
max = None
tot = 0

for num in int_vals:
    tot += num
    if min == None:
        min = num
    if max == None:
        max = num
        
    if num > max:
        max = num
    if min > num:
        min = num

print "%s %s" % (tot - max, tot - min)
