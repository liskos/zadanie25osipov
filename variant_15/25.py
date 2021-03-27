def Pr():
    k = [2]
    for x in range(3, 31197):
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            k.append(x)
    return k

def koldel(x):
    k = 0
    for i in range(2, x):
        if x % i == 0:
            k += 1
    return k


pr = Pr()
a = []
for i in range(12621, 31196, 2000):
    #
        a.append(i)
print(a)
b = 0
for i in a:
    if i not in pr:
        print(i*i, koldel(i*i))

