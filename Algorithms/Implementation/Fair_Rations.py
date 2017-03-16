#!/bin/python

import sys

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

# left to right
# if curr is OK, move to the next
# else, give curr one plus next one
# then go to next
given = 0
for x in xrange(0, N-1):
	curr = B[x]
	if curr % 2 == 0:
		continue

	B[x] += 1
	given += 2
	B[x+1] += 1

if B[N-1] % 2 != 0:
	print "NO"
	sys.exit(0)

print given

