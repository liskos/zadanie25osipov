import sys
sys.stdin = open(file='data/46/27-46b.txt')
n = int(input())
mins = 0
maxs = 0
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
for i in range(n):
    a, b = map(int, input().split())
    mins += min(a, b)
    maxs += max(a, b)
    r = abs(a - b)
    if r % 7 == 1:
        r1.append(r)
    if r % 7 == 2:
        r2.append(r)
    if r % 7 == 2:
        r2.append(r)
    if r % 7 == 3:
        r3.append(r)
    if r % 7 == 4:
        r4.append(r)
    if r % 7 == 5:
        r5.append(r)
    if r % 7 == 6:
        r6.append(r)
r1.sort()
r2.sort()
r3.sort()
r4.sort()
r5.sort()
r6.sort()
print('ost=', mins % 7, 'ch=', maxs, 'egoost=', maxs % 7, r1, r2, r3, r4, r5, r6)