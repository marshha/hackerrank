#!/bin/python
def insertionSort(ar):
	if len(ar) <= 2:
		ar.sort()
		print " ".join([ str(y) for y in ar])
		return

	for x in xrange(2, len(ar)+1):
		pre_array = ar[0:x]
		pre_array.sort()
		post_array = ar[x:len(ar)]
		out_array = pre_array + post_array
		print " ".join([ str(y) for y in out_array])
	return

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

