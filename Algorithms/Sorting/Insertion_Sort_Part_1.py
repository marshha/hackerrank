#!/bin/python
def insertionSort(ar):
	ins_pos = 0
	val = ar[-1]
	for x in xrange(0, len(ar)):
		if ar[x] > val:
			ins_pos = x
			break

	curr_array = list(ar)
	moves_list = []
	for x in reversed(range(ins_pos, len(ar))):
		move_entry = list(curr_array)
		move_entry[x] = move_entry[x-1]
		if x == ins_pos:
			move_entry[x] = val
		moves_list.append(move_entry)
		curr_array = move_entry

	moves_list_str = [ " ".join([ str(y) for y in x ]) for x in moves_list ]
	return "\n".join(moves_list_str)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)

