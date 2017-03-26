# https://www.hackerrank.com/challenges/sparse-arrays

N = int(raw_input())
given_strings = [raw_input() for i in range(N)]
some_dict = dict()
for s in given_strings:
    if s in some_dict.keys():
        some_dict[s] += 1
    else:
        some_dict[s] = 1

Q = int(raw_input())
query_strings = [raw_input() for j in range(Q)]
for q in query_strings:
    if q in some_dict.keys():
        print some_dict[q]
    else:
        print 0
