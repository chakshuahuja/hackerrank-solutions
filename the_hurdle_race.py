#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
hurdles = map(int, raw_input().strip().split(' '))

drinks_consumed = 0
current_max = k

for hurdle in hurdles:
    if hurdle <= current_max:
        continue
    else:
        drinks_consumed += (hurdle - current_max)
        current_max = hurdle

print drinks_consumed
