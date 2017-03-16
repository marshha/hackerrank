#!/bin/python

import sys


time = raw_input().strip()
tz = time[-2:]
time = time[0:-2]
time_list = time.split(":")
(hour, min, sec) = [ int(x) for x in time_list]

hour = hour % 12

if tz == "AM":
    print "%02d:%02d:%02d" % (hour, min, sec)
else:
    print "%02d:%02d:%02d" % (hour+12, min, sec)

