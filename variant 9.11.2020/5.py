def f(x):
    return int(bin(x)[2:-3])


a = []
for i in range(20, 601):
    b = f(i)
    if b not in a:
        a.append(b)
print(len(a))
