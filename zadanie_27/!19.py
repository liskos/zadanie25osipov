import sys
sys.stdin = open(file='data/19/27-19b.txt')
n = int(input())
mp = 1
p = 1
otrp = 1
for i in range(n):
    ch = int(input())
    otrp *= ch
    if ch > 0:
        p *= ch
    else:
        p = 1
    if otrp > 0:
        p = max(otrp, p)
    if p > mp:
        mp = p
print(mp)