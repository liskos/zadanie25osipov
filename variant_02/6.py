def pr(d):
    s, k = 5, 0
    while s < d:
        k += 2
        s += k
    R = s
    return R


for a in range(1,1000):
    if pr(a) == 161:
        print(a)
        break