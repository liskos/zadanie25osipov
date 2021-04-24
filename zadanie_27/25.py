import sys
sys.stdin = open(file='data/25/27-25a.txt')
n = int(input())
s = 0
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a - b)
    if r % 8 == 1:
        r1.append(r)
    if r % 8 == 2:
        r2.append(r)
    if r % 8 == 3:
        r3.append(r)
    if r % 8 == 4:
        r4.append(r)
    if r % 8 == 5:
        r5.append(r)
    if r % 8 == 6:
        r6.append(r)
    if r % 8 == 7:
        r7.append(r)
r1.sort()
r2.sort()
r3.sort()
r4.sort()
r5.sort()
r6.sort()
r7.sort()
print(s, s % 8, r1, r2, r3, r4, r5, r6, r7)