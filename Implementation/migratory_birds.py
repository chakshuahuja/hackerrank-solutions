# https://www.hackerrank.com/challenges/migratory-birds

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
count = {}
for t in types:
    if t in count.keys():
        count[t] += 1
    else:
        count[t] = 1


max_value = max(count.values())
required_keys = [k for k, v in count.iteritems() if v == max_value]
print min(required_keys)
