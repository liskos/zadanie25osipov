def f(x):
    a1 = (x // 1000) + (x // 1000 % 10)
    a2 = (x % 100 // 10) + (x % 10)
    if a1 < a2:
        return int(str(a1) + str(a2))
    else:
        return int(str(a2) + str(a1))


x = 1111
while f(x) != 1113:
    x += 1
print(x)
#долго не выдаёт ответа