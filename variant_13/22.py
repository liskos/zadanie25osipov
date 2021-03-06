def f(x):
    S = 0
    while x > 0:
        if x % 5 > 0:
            S = S + (x % 5)
        else:
            S = S * (x % 5)
        x = x // 5
    return S


k = 0
for i in range(1,501):
    if f(i) == 13:
        k +=1
print(k)
