# Enter your code here. Read input from STDIN. Print output to STDOUT
count = float(raw_input())
numbers = map(float, raw_input().split())
p = 0
n = 0
zer = 0
for num in numbers:
    if num < 0:
        n = n + 1
    elif num > 0:
        p = p + 1
    else:
        zer = zer + 1
print p/count
print n/count
print zer/count
