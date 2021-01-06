def f8(x):
    e = x % 8
    if e == 6:
        return True
    else:
        return False


def f4(x):
    f = x % 4
    if f == 2:
        return True
    else:
        return False


a = []
for i in range(4221, 17524):
    if f8(i) and f4(i):
        a.append(i)
print(sum(a), min(a))
