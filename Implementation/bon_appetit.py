# https://www.hackerrank.com/challenges/bon-appetit

n, k = map(int, raw_input().split())
costs = map(int, raw_input().split())
paid = int(raw_input())
total_to_be_paid = (sum(costs) - costs[k])/2
print "Bon Appetit" if total_to_be_paid == paid else (paid - total_to_be_paid)
