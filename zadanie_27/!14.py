import sys
sys.stdin = open(file='data/14/27-14b.txt')
n = int(input())
a = [0,0,0,0, 0,0,0,0, 0,0,0,0]
k = 0
for i in range(n):
    ch = int(input())
    ost = ch % 12
    if ost != 0:
        k += a[12 - ost]
    else:
        k += a[0]
    a[ost] += 1
print(k)
