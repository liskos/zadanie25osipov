import sys
sys.stdin = open(file='data/33/27-33b.txt')
n = int(input())
s = 0
r = [[],[],[], []]
for i in range(n):
    a, b, c = map(int, input().split())
    s += a+ b+ c - min(a, b, c)
    r1 = max(a, b, c) - min(a, b, c)
    r2 = a + b + c - max(a, b, c) - 2 * min(a, b, c)
    r[r1%4].append(r1)
    r[r2 % 4].append(r2)
print(s, s%4)
for i in range(1, 4):
    r[i].sort()
    print(i, ')', r[i])
