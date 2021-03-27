def f(a1, a2):
    a = list(range(a1, a2+1))
    k = 0
    for x in range(-1000, 1001):
        if (((x*x + x -20) >= 0) or (x not in a)) and (((x*x - 3*x -18) <= 0) or (x in a)):
            k += 1
        if k >= 10:
            return True
    return False

k = 999
for a1 in range(-10, 11):
    for a2 in range(a1, 11):
            if f(a1, a2):
                if a2 - a1 + 1 < k:
                    k = a2 - a1 + 1
print(k)
