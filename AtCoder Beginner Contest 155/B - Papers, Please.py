    n = input()
    _list = input().split(" ")
    _list = [int(x) for x in _list]
    even = [x for x in _list if x % 2==0]
    answer = []
    for x in even:
        if x % 3 == 0 or x % 5 == 0:
            answer.append(True)
    if len(even) ==len(answer):
        print("APPROVED")
    else:
        print("DENIED")
