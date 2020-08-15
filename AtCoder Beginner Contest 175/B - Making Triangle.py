from itertools import combinations
 
n = int(input())
lst = list(map(int, input().split()))
comb = combinations(lst, 3)
count = 0
 
for i in comb:
  if i[0] != i[1] and i[1] != i[2] and i[0] != i[2]:
    if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[0] + i[2] > i[1]:
      count += 1
    
print(count)
