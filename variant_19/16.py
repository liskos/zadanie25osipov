def f(n):
    if n <= 5:
        return n + 15
    if n % 2 == 0:
        return f(n//2) + n*n*n -1
    return f(n-1) + 2*n*n + 1


k = 0
for i in range(1, 1001):
    n = str(f(i))
    if '8' in n:
        n = n.replace('8', '1', 1)
        if '8' in n:
            k += 1
print(k)
