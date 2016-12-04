# Women's CodeSprint 2 : Minimum Loss
# https://www.hackerrank.com/contests/womens-codesprint-2/challenges/minimum-loss

n = int(raw_input())
numbers = map(int, raw_input().split())
d = []
for i in range(len(numbers)):
        d.append((numbers[i], i+1))
def getKey(item):
    return item[0]

d.sort(key=getKey, reverse=True)

min_loss = 10000000000000000
for i in range(n-1):
    if d[i][1] < d[i+1][1]:
        if (d[i][0] - d[i+1][0]) < min_loss:
            min_loss = d[i][0] - d[i+1][0]

print min_loss
