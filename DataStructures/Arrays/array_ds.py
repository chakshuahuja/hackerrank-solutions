# https://www.hackerrank.com/challenges/arrays-ds

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for i in range(n-1, -1, -1):
    print arr[i],
