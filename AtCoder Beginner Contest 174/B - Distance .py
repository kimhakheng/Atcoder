n, d = map(int, input().split())
count = 0
for i in range(0, n):
  x, y = map(int, input().split())
  distance = (x**2 + y**2)**(0.5)
  if distance <= d:
    count += 1
print(count)
