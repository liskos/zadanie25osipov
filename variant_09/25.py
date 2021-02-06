def f(x):
    k = 0
    max = 0
    if x %2 == 0:
        return 0, 0
    for i in range(3, int(x**0.5) +1, 2):
        if x % i == 0:
            if i == x//i:
                k += 1
            else:
                k += 2
            if k > 3:
                return max, k
            if max < x // i: max = x // i
    return max, k


for i in range(123456789, 223456790):
    max, a = f(i)
    if a == 3:
        print(max)
