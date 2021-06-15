import sys
sys.stdin = open(file='26data/26-j1.txt')
n = int(input())
a = [0] * 100
k = 0
for _ in range(n):
    a[int(input())] += 1
for i in range(1, 50):
    k += min(a[i], a[100 - i])
print(k + a[50]//2)
