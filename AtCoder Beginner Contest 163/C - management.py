N = int(input())
A = list(map(int, input().split()))
l = []
for i in range(N):
    l.append(0)
for x in A:
    l[x-1] += 1
for s in l:
    print(s)
