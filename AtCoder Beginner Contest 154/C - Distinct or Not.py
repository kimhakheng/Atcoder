    N = input()
    A = [x for x in input().split()]
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")
