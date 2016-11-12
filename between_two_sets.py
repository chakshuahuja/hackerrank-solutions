#!/bin/python
# Week of Code 25
# Problem Statement : https://www.hackerrank.com/contests/w25/challenges/between-two-sets

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def possible_values_of_x():
    return reduce(lambda x, y: x.intersection(y), [factors(i) for i in b])

print sum([set(y in factors(x) for y in a) == set([True]) for x in possible_values_of_x()])
        
