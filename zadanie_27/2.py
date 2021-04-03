import sys
sys.stdin = open(file='data/2/27-2b.txt')
n = int(input())
s = 0
minr1 = 9999999
minr1_2 = 9999999
minr2 = 9999999
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a - b)
    if r < minr1 and r % 3 ==1:
        minr1_2 = minr1
        minr1 = r
    elif r < minr1_2 and r % 3==1:
        minr1_2 = r
    if r < minr2 and r % 3 ==2:
        minr2 = r
if s%3==1:
    s-=minr1
if s%3==2:
    if minr1 + minr1_2 > minr2:
        s-=minr2
    else:
        s = s - minr1 - minr1_2
print(s)
