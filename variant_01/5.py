def alg(N):
    x = bin(N)
    x = x[2:]
    if N % 2 == 0:
        x += '01'
    else:
        x += '10'
    R = int(x,2)
    return R


for a in range(1, 1000):
    if alg(a) < 125:
        print(alg(a), a)