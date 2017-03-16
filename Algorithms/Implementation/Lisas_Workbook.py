# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
lines = sys.stdin.read()

lines_tuple = lines.split("\n")

(n, k) = lines_tuple[0].split()
t = lines_tuple[1].split()
n = int(n)
k = int(k)
t = [int(x) for x in t]

matched = 0
page_num = 1
for chapter in xrange(1,n+1):
    pages_in_chapter = t[chapter-1] / k
    if t[chapter-1] % k != 0:
        pages_in_chapter += 1
    for i in xrange(0,pages_in_chapter):
        lowest_q = ((i)*k) + 1
        highest_q = min((i+1)*k, t[chapter-1])
        #print "page %s, range: %s %s" % (page_num, lowest_q, highest_q )
        if page_num <= highest_q and page_num >= lowest_q:
            #print "page matched: page %s, chapter %s" % (page_num, chapter)
            matched += 1
        page_num += 1

print matched
        
