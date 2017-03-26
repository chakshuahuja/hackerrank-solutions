# https://www.hackerrank.com/challenges/2d-array

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
    
max_sum = -100
for i in xrange(4):
    for j in xrange(4):
        curr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if curr_sum > max_sum:
            max_sum = curr_sum
print max_sum
