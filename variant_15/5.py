def f(x):
    x10 = x
    x8 = ''
    while x >0:
        x8 += str(x%8)
        x = x//8
    x8 = int(x8, 8)
    return x10 - x8


m = 0
for i in range(10, 100):
    f = f(i)
    if f > m:
        m = f
print(m)
