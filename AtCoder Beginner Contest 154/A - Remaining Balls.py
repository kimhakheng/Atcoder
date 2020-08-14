    S, T = input().split()
    A, B = input().split()
    U = input()
    A, B = int(A), int(B)
     
    if U == S:
        A -= 1
    elif U == T:
        B -= 1
     
    print(A,B)
