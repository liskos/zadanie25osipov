def f(x):
    k = 0
    max = 0
    if x %2 == 0:
        return 0, 0
    c = int(x**0.5)
    c2 = c//2
    for i in range(3, c +1, 2):
        if x % i == 0:
            if x % (i*i) == 0 and i < c2:
                return 0, 0
            m = x//i
            if i == m:
                k += 1
            else:
                k += 2
                if k > 3:
                    return 0, 0
            if max < m: max = m
    return max, k


for i in range(123456789, 223456790):
    max, a = f(i)
    if a == 3:
        print(max)
