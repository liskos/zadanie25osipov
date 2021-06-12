import sys

sys.stdin = open(file='data/39/27-39b.txt')
n = int(input())
a = [0] * 1000
for _ in range(n):
    a[int(input())] += 1
otv = 0
for i in range(100, 1000):
    not_i = int(str(i)[::-1])
    if i != not_i:
        m = min(a[i], a[not_i])
        otv += m * sum(map(int, str(i)))
        a[i] = a[i] - m
        a[not_i] = a[not_i] - m
    else:
        m = a[i] // 2
        otv += m * sum(map(int, str(i)))
        a[i] = a[i] - m * 2
r = max([i for i in range(100, 1000) if str(i) == str(i)[::-1] and a[i] != 0])
print(otv * 2 + sum(map(int, str(r))))
