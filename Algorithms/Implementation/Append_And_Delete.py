#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

matched_pos = None
req_moves = 0

# Find the first match
for x in xrange(0, len(s)):
	if s[x] == t[x]:
		matched_pos = x

	if s[x] != t[x]:
		break

	# if the end of t is reached, it's a complete match
	if x == len(t) - 1:
		break

# now find the moves required to match s and t
if matched_pos == None:
	req_moves = len(s) + len(t)
	if req_moves <= k:
		print "Yes"
	else:
		print "No"
	sys.exit(0)

if k > (len(t) + len(s)):
	print "Yes"
	sys.exit(0)

# determine number of characters to be removed
# from t
t_remove = (len(t) -1) - matched_pos

# determine number of characters to add
# from s
s_add = (len(s) - 1) - matched_pos
req_moves = t_remove + s_add
#print matched_pos, req_moves, t_remove, s_add
if k >= req_moves:
	if ((k - req_moves) % 2) == 0:
		print "Yes"
		sys.exit(0)

print "No"
sys.exit(0)
