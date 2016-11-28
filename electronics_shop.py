#!/bin/python
# Women's CodeSprint 2
# Problem Statement : https://www.hackerrank.com/contests/womens-codesprint-2/challenges/electronics-shop
import sys

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int,raw_input().strip().split(' '))
pendrives = map(int,raw_input().strip().split(' '))
cost = 0
for i in range(len(keyboards)):
    for j in range(len(pendrives)):
        temp = keyboards[i] + pendrives[j]
        if temp <= s and temp > cost:
            cost = temp
if cost:
    print cost
else:
    print -1
