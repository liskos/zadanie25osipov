def f(n):
    if n <= 18:
        return n + 3
    if n % 3 != 0:
        return f(n - 1) + n * n + 5
    return (n // 3) * f(n // 3) + n - 12


k = 0
for i in range(1, 1001):
    s = set(str(f(i)))
    if s <= {'2', '4', '6', '8', '0'}:
        k += 1
print(k)
