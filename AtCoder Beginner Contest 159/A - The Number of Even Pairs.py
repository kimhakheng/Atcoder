from itertools import combinations

N, M = map(int, input().split())

a = list(combinations(range(N), 2))
b = list(combinations(range(M), 2))
print(len(a)+len(b))
