# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(raw_input())
for i in range(test_cases):
    length = int(raw_input())
    numbers = map(int, raw_input().split())
    non_contiguous_sum = 0
    contiguous_sum = 0
    for num in numbers:
        if num > 0:
            non_contiguous_sum = non_contiguous_sum + num
    best_sum = 0
    curr_sum = 0
    start = -1
    end = -1
    curr_index = -1
    for i in range(length):
        val = curr_sum + numbers[i]
        if val > 0:
            if curr_sum == 0:
                curr_index = i
            curr_sum = val
        else:
            curr_sum = 0
        if curr_sum > best_sum:
            best_sum = curr_sum
            start = curr_index
            end = i
    contiguous_sum = best_sum

    if non_contiguous_sum == 0:
        non_contiguous_sum = max(numbers)
        contiguous_sum = max(numbers)
    print contiguous_sum, non_contiguous_sum
