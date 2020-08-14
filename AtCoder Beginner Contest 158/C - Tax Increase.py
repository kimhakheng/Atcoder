a, b = [int(x) for x in input().split()]

if (b < a):
    temp = b
    b = a
    a = temp
x = 1
while True:
    if (int(x*0.08) == a and int(x*0.1) == b):
        print(x)
        break
    else:
        if (x > 1500):
            print(-1)
            break
        else:
            x += 1
