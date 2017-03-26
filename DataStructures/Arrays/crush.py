# https://www.hackerrank.com/challenges/crush

N, M = map(int, raw_input().split())
L = [0 for _ in xrange(N+1)]
for _ in xrange(M):
    a, b, k = map(int, raw_input().split())
    L[a-1] += k
    L[b] -= k

max_value = 0
cur_max = 0
for val in L:
    cur_max = cur_max + val
    if cur_max > max_value:
        max_value = cur_max
    
print max_value
