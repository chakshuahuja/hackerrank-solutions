# https://www.hackerrank.com/challenges/mini-max-sum
import sys

numbers = map(int, raw_input().strip().split(' '))
max_sum = 0
min_sum = 10000000000
for i in range(5):
    curr_sum = sum(numbers) - numbers[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < min_sum:
        min_sum = curr_sum

print min_sum, max_sum