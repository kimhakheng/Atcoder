n = int(input())
list = []
for a in range(1,n+1):
    if a % 3 == 0 or a % 5 == 0:
        pass
    else:
        list.append(a)
print(sum(list))
