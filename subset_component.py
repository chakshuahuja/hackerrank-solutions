import re
import itertools
N = int(raw_input())
numbers = map(int, raw_input().split(' '))
def generateSubsets(numbers):
    result = [[]]
    for x in numbers:
        result.extend([subset + [x] for subset in result])
    return result

#Implementing Graph Traversal DFS Recursive
def DFSRecursive(G, s, visited_recursive):
    visited_recursive[s] = True
    for w in G[s]:
        if not visited_recursive[w]:
            DFSRecursive(G, w, visited_recursive)

#Finding the number of components using DFS
def noOfComponents(G, visited_recursive):
    no_of_components = 0
    for i in range(64):
        if not visited_recursive[i]:
            DFSRecursive(G, i, visited_recursive)
            no_of_components += 1
    return no_of_components

def solve(numbers):
    adj_list = {}
    no_of_nodes = 64

    for i in range(no_of_nodes):
        adj_list[i] = []
    components = 64
    for number in numbers:
        visited_recursive = []
        for i in range(64):
            visited_recursive.append(False)

        bin_number = bin(number)[2:].zfill(64)
        count1s = [m.start() for m in re.finditer('1', bin_number)]
        pairs = list(itertools.combinations(count1s, 2))
        for pair in pairs:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
    
        components = noOfComponents(adj_list, visited_recursive)
    return components

subsets = generateSubsets(numbers)
sum_of_components = 0
for subset in subsets:
    sum_of_components = sum_of_components + solve(subset)

print sum_of_components
