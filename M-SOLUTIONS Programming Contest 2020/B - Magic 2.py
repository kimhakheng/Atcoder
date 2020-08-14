a, b, c = map(int, input().split())
k = int(input())

n = 0
while b <= a:
  b = b*2
  n += 1
while c <= b:
  c = c*2
  n += 1
if n <= k:
  print("Yes")
else:
  print("No")
