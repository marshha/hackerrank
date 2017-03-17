def insertionSort(ar):
	moves = 0
	final_array = list(ar)
	for x in xrange(1, len(ar)):
		curr = final_array[x]
		ins_pos = 0
		for y in reversed(xrange(0, x)):
			if final_array[y] <= curr:
				ins_pos = y+1
				break
		if ins_pos < x:
			moves += (x - ins_pos)
			final_array.pop(x)
			final_array.insert(ins_pos, curr)
			#print "Remove %s from %s and ins at %s" % (curr, x, ins_pos)
		
	return moves

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)

