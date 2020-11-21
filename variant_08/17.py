def thirty_four(x):
    return int(str(x)[-4:-2]) < 50


def mod(x):
    a1 = str(x)[:3]
    a2 = str(x)[-3:]
    return int(a1) % 5 == int(a2) % 5


k = 0
b = 0
for a in range(246815, 875622):
    if thirty_four(a) and mod(a):
        k += 1
        b = a
print(b, k)
