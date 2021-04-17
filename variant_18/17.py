def f(x):
    a = []
    for i in x:
        a.append(int(i))
    r = max(a) - min(a)
    if r < 4:
        return True
    return False


a = []
for i in range(1005, 147871):
    x = str(i)
    if '1' not in x and f(x):
        a.append(i)
a.sort(reverse=True)
print(len(a), a[24])
