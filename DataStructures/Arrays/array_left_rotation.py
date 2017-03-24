# https://www.hackerrank.com/challenges/array-left-rotation

n, d = map(int, raw_input().split())
numbers = map(int, raw_input().split())

lr = d%n
for i in range(n):
    print numbers[(lr-n+i)%n],
