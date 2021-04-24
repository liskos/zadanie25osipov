import sys
sys.stdin = open(file='data/48/27-48a.txt')
n = int(input())
s = 0
kch = 0
knech = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        s += a
        r = a - b
        if a % 2 == 0:
            kch += 1
        else:
            knech += 1
    else:
        s += b
        r = b - a
        if b % 2 == 0:
            kch += 1
        else:
            knech += 1
    if minr > r and r % 2 != 0:
        minr = r
print(s, 'ch=', kch, 'nech=', knech, minr)