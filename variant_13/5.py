def f(x):
    x = str(x)
    a = []
    for i1 in x:
        for i2 in x:
            if i1 != i2 or ((i2 in x.replace(i1, 'n', 1)) and (i1 == i2)):
                if len(str(int(i1 + i2))) == 2:
                    a.append(int(i1 + i2))
    if len(a) > 1:
        return len(a)



n = 999
N = 0
for i in range(1000, 10000):
    k = f(i)
    if k > n :
        n = k
print(n)
    #???