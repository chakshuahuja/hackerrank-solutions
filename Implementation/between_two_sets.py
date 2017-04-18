# https://www.hackerrank.com/challenges/between-two-sets

n, m = map(int, raw_input().strip().split(' '))
A = map(int, raw_input().strip().split(' '))
B = map(int, raw_input().strip().split(' '))


def find_factors(x):
    return [i for i in xrange(1, x+1) if x % i == 0]

all_factors = {b: find_factors(b) for b in B}
common_factors = list(reduce(set.intersection, [set(item) for item in all_factors.values()]))
print sum([(set(A) - set(find_factors(cf)) == set()) for cf in common_factors])