# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
sum_d1 = 0
sum_d2 = 0
for i in range(N):
    int_l = map(int, raw_input().split())
    sum_d1 = sum_d1 + int_l[i]
    sum_d2 = sum_d2 + int_l[N-1-i]
   
print abs(sum_d1 - sum_d2)
