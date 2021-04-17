def f(x):
    k = 0
    for i in range(3, x):
        if x % i == 0:
            return False
    return True


for i in range(103, 112, 2):
    if f(i):
        print(i**4, i**3)