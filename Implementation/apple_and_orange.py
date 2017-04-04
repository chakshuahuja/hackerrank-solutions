# https://www.hackerrank.com/challenges/apple-and-orange

import sys

s, t = map(int, raw_input().strip().split(' '))
a, b = map(int, raw_input().strip().split(' '))
m, n = map(int, raw_input().strip().split(' '))

apples = map(int, raw_input().strip().split(' '))
oranges = map(int, raw_input().strip().split(' '))
apples_coords = [i + a for i in apples]
oranges_coords = [i + b for i in oranges]
apples_in_house = [i >= s and i <= t for i in apples_coords]
oranges_in_house = [i >= s and i <= t for i in oranges_coords]
print sum(apples_in_house)
print sum(oranges_in_house)