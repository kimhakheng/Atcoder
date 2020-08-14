s = str(input()).lower()
t = str(input()).lower()
if t.find(s) == 0 and len(t) == len(s) + 1 :
    print('Yes')
else:
    print('No')
