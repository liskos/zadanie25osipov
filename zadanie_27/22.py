import sys
sys.stdin = open(file='data/22/27-22b.txt')
n = int(input())
s = 0
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r % 10 == 1:
        r1.append(r)
    if r % 10 == 2:
        r2.append(r)
    if r % 10 == 3:
        r3.append(r)
    if r % 10 == 4:
        r4.append(r)
    if r % 10 == 5:
        r5.append(r)
    if r % 10 == 6:
        r6.append(r)
    if r % 10 == 7:
        r7.append(r)
    if r % 10 == 8:
        r8.append(r)
    if r % 10 == 9:
        r9.append(r)
r1.sort()
r2.sort()
r3.sort()
r4.sort()
r5.sort()
r6.sort()
r7.sort()
r8.sort()
r9.sort()
print(s, r1, r2, r3, r4, r5, r6, r7, r8, r9)