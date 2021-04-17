def f(n):
    if n <= 18:
        return n+3
    if n % 3 != 0:
        return f(n-1) + n*n + 5
    return (n//3)*f(n//3) + n - 12


k = 0
for i in range(1, 1001):
    s = str(f(i))
    if '1' not in s and '3' not in s and '5' not in s and '7' not in s and '9' not in s:
        k += 1
print(k)
