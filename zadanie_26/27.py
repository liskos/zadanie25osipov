import sys
sys.stdin = open(file='26data/26-j2.txt')
n, k, t = int(input()), 0, 0
a = sorted([int(input()) for _ in range(n)])
sr = sum(a) // n
while a[k] <= sr:
    k += 1
med = a[k + (n - k) // 2]
for i in range(k, k + (n - k) // 2):
    if a[i] != sr and a[i] != med:
        t += 1
print(t)
