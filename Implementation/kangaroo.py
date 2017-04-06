# https://www.hackerrank.com/challenges/kangaroo

import sys

x1, v1, x2, v2 = map(int, raw_input().strip().split(' '))
if v1 <= v2:
    print "NO"
else:
    if ((x2-x1) % (v1-v2) == 0):
        print "YES"
    else:
        print "NO"
