def delit(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0:
            k+=1
    return k

a = []
kmax = 0
for i in range(541, 1235):
    if delit(i) > delit(kmax):
        kmax = i
print(delit(kmax), kmax)