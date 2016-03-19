# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_children = int(raw_input())
rating = []
for i in range(no_of_children):
    rating.append(int(raw_input()))
chocolates = []
for i in range(no_of_children):
    chocolates.append(0)
for i in range(no_of_children):
    if i == 0:
        chocolates[i] = 1
    if rating[i] > rating[i-1]:
        chocolates[i] = chocolates[i-1] + 1
    elif rating[i] == rating[i-1]:
        chocolates[i] = 1
    else:
        chocolates[i] = 1
        j = i
        while chocolates[j-1] <= chocolates[j] and j >= 0 and rating[j-1] > rating[j]:
            chocolates[j-1] += 1
            j = j - 1
        
print sum(chocolates)
