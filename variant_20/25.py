def delit(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return i + (x//i)
    return 0


s = 452021
k = 0
while k != 5:
    s += 1
    d = delit(s)
    if d % 7 == 3:
        print(s, d)
        k += 1
