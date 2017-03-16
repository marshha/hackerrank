#!/bin/python

import sys
import math

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
c.sort()
prev_idx = c[0]
max_dist = None
    
for idx in c[1:]:
    dist = idx - prev_idx
    if max_dist == None:
        max_dist = dist
    if max_dist < dist:
        max_dist = dist
    prev_idx = idx

if max_dist:
    max_dist = int(math.ceil(float(max_dist/2)))

dist = (n-1) - c[-1]
if max_dist == None:
    max_dist = dist
if dist > max_dist:
    max_dist = dist

dist = c[0]
if max_dist == None:
    max_dist = dist
if dist > max_dist:
    max_dist = dist

print max_dist
