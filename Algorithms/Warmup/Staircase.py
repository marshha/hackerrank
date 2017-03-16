 #!/bin/python

import sys


n = int(raw_input().strip())

for x in xrange(1,n+1):
    spaces = ''.join([ ' ' for i in xrange(0,n-x)])
    hashes = ''.join([ '#' for i in xrange(0,x)])
    print "%s%s" % (spaces, hashes)
