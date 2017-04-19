# https://www.hackerrank.com/challenges/divisible-sum-pairs

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))

count = 0
for i in xrange(n-1):
    for j in xrange(i+1, n):
        if (a[i]+a[j]) % k == 0:
            count += 1

print count
