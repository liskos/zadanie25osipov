def f(x):
    if x % 2 == 1:
        for i in range(71, int(x ** 0.5)):
            if x % i == 0:
                return 1
            else:
                return 0
    else:
        return 0


k = 0
for i in range(654321, 987124):
    k += f(i)
print(k)
