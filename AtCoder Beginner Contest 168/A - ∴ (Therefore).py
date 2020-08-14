N = int(input())
hon = '24579'
pon = '0168'
bon = '3'
n = str(N)[::-1]
for i in n:
    if i in hon:
        print ("hon")
        break
    if i in pon:
        print ("pon")
        break
    if i in bon:
        print ("bon")
        break
