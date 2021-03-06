def f(x):
    a1 = x//100
    a2= x%100
    if len(str(a1)) == 2 and len(str(a2)) == 2 and abs(a1 - a2) > 70:
        return True
    return False


a = []
for i in range(1032, 8416):
    ifs = f(i)
    if ifs:
        a.append(i)
print(max(a), len(a))
