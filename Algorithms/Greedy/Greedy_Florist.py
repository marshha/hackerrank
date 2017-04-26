#!/bin/python
# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
    C.append( int(number) )
    i = i+1

C = sorted(C, reverse=True)
result = 0
cnt = 0

for x in xrange(0, len(C)):
    if (x % K) == 0:
        cnt += 1

    result += C[x] * (cnt)

print result

