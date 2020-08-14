    n, a, b = map(int, input().split())
    period = a+b
    times = n//period
    k = n%period
    n =  a if k >a else k
    print(times*a + n)
