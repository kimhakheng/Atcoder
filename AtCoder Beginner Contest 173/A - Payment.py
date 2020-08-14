n = int(input())
if n > 0:
  if n % 1000 == 0:
    print(0)
  else:
    print(int(1000 - (n%1000)))
