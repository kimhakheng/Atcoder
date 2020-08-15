s = input().upper()
if s.count('RRR') == 1:
  print(3)
elif s.count('RR') == 1:
  print(2)
elif s.count('R') > 0:
  print(1)
else:
  print(0)
