import sys
sys.stdin = open(file='26data/26-J5.txt')
n = int(input())
a = [int(input()) for _ in range(n)]
v = 0
b = [a[0]]
for i in range(1, n-1):
    c = sorted([a[i - 1], a[i], a[i + 1]])
    b.append(c[1])
    if a[i] > c[1]:
        v += a[i] - c[1]
b = b + [a[-1]]
print(v)
print(b.count(min(b)))