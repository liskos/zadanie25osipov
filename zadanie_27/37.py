import sys
sys.stdin = open(file='data/37/27-37b.txt')
n = int(input())
a = [0] * 10001
k = 0
for _ in range(n):
    x = int(input())
    for i in range(1, (x // 2) + 1):
        if i == x - i:
            k += (a[i] * (a[i] - 1)) // 2
        else:
            k += a[i] * a[x - i]
    a[x] += 1
print(k)
