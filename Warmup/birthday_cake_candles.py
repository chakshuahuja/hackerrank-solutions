# https://www.hackerrank.com/challenges/birthday-cake-candles

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
max_height = max(height)
matching = sum([height[i]==max_height for i in xrange(n)])
print matching
