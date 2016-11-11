T = int(raw_input())
for t in range(T):
    M = int(raw_input())
    N = int(raw_input())
    numbers = map(int, raw_input().split())
    store = {}
    for i in range(N):
        store[numbers[i]] = i+1
    for i in range(N):
        if M - numbers[i] in store.keys() and store[M-numbers[i]] != i+1:
            print i+1, store[M-numbers[i]]
            break
