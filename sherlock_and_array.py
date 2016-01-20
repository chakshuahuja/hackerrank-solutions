# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    numbers = map(int, raw_input().split())
    cum_sum_array_begin_to_end = []
    cum_sum_array_end_to_begin = []
    for i in range(N):
        cum_sum_array_begin_to_end.append(0)
        cum_sum_array_end_to_begin.append(0)
    cum_sum_array_begin_to_end[0] = numbers[0]
    cum_sum_array_end_to_begin[N-1] = numbers[N-1]
    for i in range(1, N):
        cum_sum_array_begin_to_end[i] = numbers[i] + cum_sum_array_begin_to_end[i-1]
    for i in range(N-2, -1, -1):
        cum_sum_array_end_to_begin[i] = numbers[i] + cum_sum_array_end_to_begin[i+1]
    flag = 0
    for i in range(N):
        if cum_sum_array_begin_to_end[i] == cum_sum_array_end_to_begin[i]:
            flag = 1
            break
    if flag == 1:
        print 'YES'
    else:
        print 'NO'
