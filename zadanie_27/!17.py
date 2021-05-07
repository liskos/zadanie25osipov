import sys
sys.stdin = open(file='data/17/27-17b.txt')
n = int(input())
a = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0]
r = [0,0,0,0,0]
k = 0
for i in range(n):
    r.append(int(input()))
    ost = r[5] % 13
    if ost != 0:
        k += a[13 - ost]
    else:
        k += a[0]
    a[r[0]%13] += 1
    r.pop(0)
print(k)
