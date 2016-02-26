# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import itertools
from copy import copy
N = int(raw_input())
numbers = map(int, raw_input().split(' '))
def find1sSet(num):
    return set([m.start() for m in re.finditer('1', bin(num)[2:][::-1])])
    
def merge(a, b):
    overlap = False
    union = copy(a)
    for ele in b:
        if ele in a:
            overlap = True
        else:
            union.add(ele)
    return (union, overlap)

def solve(start, n, prev, prevContri):
    ans = 0
    for i in range(start, n):
        component = sets[i]
        if len(component) > 1:
            (newBits, overlap) = merge(prev, component)
            if len(prev) == 0 or overlap:
                contri = 64 - len(newBits) + 1
            else:
                contri = prevContri + 1 - len(component) 
        else:
            (newBits, contri) = (prev, prevContri)
        ans += contri + solve(i+1, n, newBits, contri)
    return ans
  

sets = []
for number in numbers:
    set1s = find1sSet(number)
    sets.append(set1s)
    
print 64 + solve(0, N, set(), 64)
