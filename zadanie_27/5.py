import sys
sys.stdin = open(file='data/5/27-5b.txt')
n = int(input())
minr1 = [9999, 10000, 10001, 10002]
minr2 = [9999, 10000]
minr3 = 9999
minr4 = 9999
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r % 5 == 1 and r < minr1[3]:
        minr1.append(r)
        minr1.sort()
        minr1.pop(4)
    elif r % 5 == 2 and r < minr2[1]:
        minr2.append(r)
        minr2.sort()
        minr2.pop(2)
    elif r % 5 == 3 and r < minr3:
        minr3 = r
    elif r % 5 == 4 and r < minr4:
        minr4 = r
if s % 5 == 1:
    s += min(minr4, (minr3 + minr1[0]), sum(minr2), sum(minr1))
elif s % 5 == 2:
    s += min(minr3, (minr2[0] + minr1[0]), (minr1[0] + minr1[1] + minr1[2]))
elif s % 5 == 3:
    s += min(minr2[0], (minr1[0] + minr1[1]))
elif s % 5 == 4:
    s += minr1[0]
print(s)
