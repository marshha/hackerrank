#!/bin/python

import sys

in_str = raw_input().strip()
out_arr = []

for x in xrange(0, len(in_str)):
        out_arr.append(in_str[x])
        if len(out_arr) > 1:
            if out_arr[-1] == out_arr[-2]:
                out_arr = out_arr[0:-2]

if out_arr:
    print "".join(out_arr)
else:
    print "Empty String"
