# https://www.hackerrank.com/challenges/dynamic-array

N, Q = map(int, raw_input().split())
L = [[] for _ in range(N)]
lastAns = 0
for _ in xrange(Q):
    n, x, y = map(int, raw_input().split())
    if n == 1:
        seq_number = (x^lastAns) % N
        L[seq_number].append(y)
    if n == 2:
        seq_number = (x^lastAns) % N
        lastAns = L[seq_number][y % len(L[seq_number])]
        print lastAns
