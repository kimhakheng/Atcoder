    b = input()
    a = b.split(" ")
    N, R = (int(x) for x in b.split(" "))
    if N>= 10:
      I = R
      print(I)
    else:
      I = R + 100*(10-N)
      print(I)
