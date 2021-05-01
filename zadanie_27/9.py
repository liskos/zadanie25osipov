import sys
sys.stdin = open(file='data/9/27-9b.txt')
n = int(input())
a = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
minp = 99999999
for i in range(6, n):
    a.append(int(input()))
    p = a[i] * min(a[:i-5])
    if p < minp and p % 2 == 1:
        minp = p
if minp == 99999999:
    print(-1)
else:
    print(minp)
