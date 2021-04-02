def ndel():
    a = [2,3]
    for i in range(4, 1235):
        for d in a:
            if i%d == 0:
                continue
        a.append(i)
    return a


def delit(n, x):
    k = 0
    for i in n:
        if x % i == 0:
            k+=1
    return k


n = ndel()
for i in range(541, 1235): #!!!!