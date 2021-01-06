def f(x):
    n = bin(x)
    n = n[2:]
    s = 0
    for i in n:
        s += int(i)
    s = s % 2
    if s == 1:
        return x * 4 + 2
    else:
        return x * 4



i = 1
while f(i) <= 105:
    i += 1
print(i)
