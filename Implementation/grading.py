# https://www.hackerrank.com/challenges/grading

import sys

n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    if grade < 38:
        print grade
        continue
    difference = 5 - (grade % 5)
    if difference < 3:
        print grade+difference
    else:
        print grade
