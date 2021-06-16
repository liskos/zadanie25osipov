def f(n):
    s = bin(n)[2:]
    s = s + str(sum(map(int, s)) % 2)
    s = s + str(sum(map(int, s)) % 2)
    return int(s, 2)


for i in range(1, 100000):
    if f(i) > 125:
        print(i)
        break
