n = int(input())
AC, WA, TLE, RE = 0, 0, 0, 0
while n != 0:
  i = input()
  if i == 'AC':
    AC += 1
  elif i == 'WA':
    WA += 1
  elif i == 'TLE':
    TLE += 1
  elif i == 'RE':
    RE += 1
  n -= 1
print("AC x",AC)
print("WA x",WA)
print("TLE x",TLE)
print("RE x",RE)
