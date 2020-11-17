def f(x):
    a = []
    if x % 25 == 0 or x % 49 == 0 or x % 169:
        return False, 0
    for k in range(2, int(x ** 0.5 + 1)):
        if x % k == 0:
            a.append(k)
            a.append(x // k)
    m = max(a)
    if m < 100001:
        return True, m
    else:
        return False, 0


for i in range(224466, 664423):
    tf, M = f(i)
    if i % 5 == 0 and i % 7 == 0 and i % 13 == 0 and tf:
        if M % 100 == 19:
            print(i, M)
# программа не находит искомые числа, но, кажется, работает коректно, так что, вероятно: что-то упускаю.