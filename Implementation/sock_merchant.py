# https://www.hackerrank.com/challenges/sock-merchant

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))
socks = {}
for i in c:
    if i in socks.keys():
        socks[i] += 1
    else:
        socks[i] = 1

print sum([s/2 for s in socks.values()])
