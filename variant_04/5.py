def F(x):
    x = bin(x)
    x = x[2:]
    x = x.replace('1', '2')
    x = x.replace('0', '1')
    x = x.replace('2', '0')
    R = int(x, 2)
    return R + 1


for i in range(257):
    print(F(i), i)
    if F(i) == 221:
        break
