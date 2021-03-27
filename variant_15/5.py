def fun(x):
    x10 = x
    x8 = ''
    for i in range(8):
        x8 += str(x%2)
        x = x//2
    x8 = int(x8, 2)
    return x10 - x8


m = 0
for i in range(1, 256):
    f = fun(i)
    if f > m:
        m = f
print(m)
