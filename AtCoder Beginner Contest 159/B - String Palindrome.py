s = input()
if s == s[::-1]:
    flag = True
else:
    flag = False
N = len(s)
if flag:
    new = s[0:int((N-1)/2)]
    if new == new[::-1]:
        flag = True
    else: flag = False

if flag:
    new = s[int((N+2)/2):N]
    if new == new[::-1]:
        flag = True
    else:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
