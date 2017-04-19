# https://www.hackerrank.com/challenges/the-birthday-bar


def getWays(squares, d, m):
    count = 0
    for i in xrange(len(squares)-m+1):
        count += int(sum(squares[i:i+m]) == d)
    return count

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = map(int, raw_input().strip().split(' '))
result = getWays(s, d, m)
print(result)
