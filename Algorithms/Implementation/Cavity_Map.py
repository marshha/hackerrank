#!/bin/python

import sys

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
	grid_t = str(raw_input().strip())
	grid.append(grid_t)

matched_rows = {}

# skip row 1
row_val = 1
for row in grid[1:n-1]:
	char_row = [ int(x) for x in list(row) ]
	for x in xrange(1, n-1):
		if (char_row[x-1] < char_row[x] and
			char_row[x+1] < char_row[x] and
			int(grid[row_val-1][x]) < char_row[x] and
			int(grid[row_val+1][x]) < char_row[x]):
			if row_val not in matched_rows:
				matched_rows[row_val] = []
			matched_rows[row_val].append(x)

	row_val += 1

grid_iter = 0
output_list = []
for grid_row in grid:
	output = ""
	for grid_row_iter in xrange(0, len(list(grid_row))):
		output_char = None
		if grid_iter in matched_rows:
			if grid_row_iter in matched_rows[grid_iter]:
				output_char = "X"

		if output_char == None:
			output_char = grid_row[grid_row_iter]

		output += output_char
	grid_iter += 1
	output_list.append(output)

print "\n".join(output_list)

