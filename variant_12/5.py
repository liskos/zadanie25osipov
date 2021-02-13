def f(n):
    if n % 2 == 0:
        return n * 4 + 1
    else:
        return n * 4 + 2


a = []
for i in range(32):
    if f(i) > 102:
        a.append(f(i))
print(min(a))
