import sys
sys.stdin = open(file='26data/26-j6.txt')
n = int(input())
a = sorted([int(input()) for _ in range(n)])
v = int(0.9 * sum(a))
k, m, s = 0, 0, 0
for i in range(n):
    if s + a[i] <= v:
        s += a[i]
        m = a[i]
        k += 1
    else:
        break
print(k, m)
