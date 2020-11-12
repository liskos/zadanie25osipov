def thirty_four(x):
    x = str(x // 1000 % 10) + str(x // 100 % 10)
    if int(x) < 50:
        return True
    else:
        return False


def mod(x):
    a1, a2 = x // 1000, x % 1000
    if a1 % 5 == a2 % 5:
        return True
    else:
        return False


k = 0
b = 0
for a in range(24615, 875622):
    if thirty_four(a) and mod(a):
        k += 1
        b = a
print(k, a)
