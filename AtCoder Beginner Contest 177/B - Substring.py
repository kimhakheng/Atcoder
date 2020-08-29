s = input()
t = input()
res = []
for i in range(len(s)-len(t)+1):
    x = s[i:i+len(t)]
    count = sum(1 for a, b in zip(t, x) if a != b)
    res.append(count)
print(min(res))
