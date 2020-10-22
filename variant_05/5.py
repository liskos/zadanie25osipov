def f(x):
    x = int(str(x) + str(x % 10))
    x = bin(x)
    x = str(x[2:])
    k = 0
    for i in x:
        if i == 1: k += 1
    x += str(k % 2)
    return int(x, 2)


for i in range(255):
    if f(i) > 413:
        print(i)
        break
