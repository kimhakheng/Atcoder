k,n = map(int, input().split())
lst = list(map(int, input().split()))

maxDis = (k-lst[-1]) + lst[0]
for i in range(n-1):
  if lst[i+1] - lst[i] > maxDis:
    maxDis = lst[i+1] - lst[i]
print(k-maxDis)
