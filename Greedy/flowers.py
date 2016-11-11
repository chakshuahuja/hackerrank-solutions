N, K = raw_input().split()
N = int(N)
K = int(K)

numbers = map(int, raw_input().split())
numbers.sort(reverse=True)
no_of_complete  = N / K
remaining = N % K
result = 0
j = 0
for i in range(no_of_complete):
    j = i*K
    for m in range(K):
        result += ((i+1)*numbers[j+m])
       
j = no_of_complete*K
for i in range(remaining):
    result += ((no_of_complete+1)*numbers[j])
    j += 1

print result

