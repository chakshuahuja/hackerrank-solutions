a, b, num = map(int, raw_input().split())
l = []
for i in range(num):
    l.append(-1)
l[0] = a
l[1] = b
def modified_fibo(num):
    if l[num] != -1:
        return l[num]
    else:
        l[num] = modified_fibo(num-1)**2 + modified_fibo(num-2)
    return l[num]
print modified_fibo(num-1)
