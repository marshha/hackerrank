#!/usr/bin/python
N = input()
K = input()
lists = [int(input()) for _ in range(0,N)]
diffs = []
lists.sort()
for x in xrange(K-1, len(lists)):
    diffs.append(abs(lists[x-(K-1)] - lists[x]))

min_diff = min(diffs)
print min_diff

