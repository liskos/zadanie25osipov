import sys
sys.stdin = open(file='data/32/27-32b.txt')
n = int(input())
s = 0
r = [[],[],[], [],[],[], [],[],[], [],[]]
for i in range(n):
    a, b, c = map(int, input().split())
    s += min(a, b, c)
    r1 = max(a, b, c) - min(a, b, c)
    r2 = a + b + c - max(a, b, c) - 2 * min(a, b, c)
    r[r1%11].append(r1)
    r[r2 % 11].append(r2)
print(s, s%11)
for i in range(1, 11):
    r[i].sort()
    print(i, ')', r[i])
