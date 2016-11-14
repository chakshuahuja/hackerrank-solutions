#  Adobe CODHERS Codesprint
# Problem Statement : https://www.hackerrank.com/contests/adobe-codhers/challenges/jesse-loves-candy
# TIP: Do not assume that taking candy from first shop will be the fastest
N, k = map(int, raw_input().split())
b = map(int, raw_input().split())
candies = [i for i in range(N) if b[i] == 1]
diff = [t - s for s, t in zip(candies, candies[1:])]
print min(candies[i]+k*diff[i] for i in range(len(diff)))
