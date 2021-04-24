import sys
sys.stdin = open(file='data/26/27-26b.txt')
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
r10 = []
r11 = []
r12 = []
r13 = []
r14 = []
r15 = []
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r % 16 == 1:
        r1.append(r)
    if r % 16 == 2:
        r2.append(r)
    if r % 16 == 3:
        r3.append(r)
    if r % 16 == 4:
        r4.append(r)
    if r % 16 == 5:
        r5.append(r)
    if r % 16 == 6:
        r6.append(r)
    if r % 16 == 7:
        r7.append(r)
    if r % 16 == 8:
        r8.append(r)
    if r % 16== 9:
        r9.append(r)
    if r % 16 == 10:
        r1.append(r)
    if r % 16 == 11:
        r2.append(r)
    if r % 16 == 12:
        r3.append(r)
    if r % 16 == 13:
        r4.append(r)
    if r % 16 == 14:
        r5.append(r)
    if r % 16 == 15:
        r6.append(r)
r1.sort()
r2.sort()
r3.sort()
r4.sort()
r5.sort()
r6.sort()
r7.sort()
r8.sort()
r9.sort()
r10.sort()
r11.sort()
r12.sort()
r13.sort()
r14.sort()
r15.sort()
print(s, s%16, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15)