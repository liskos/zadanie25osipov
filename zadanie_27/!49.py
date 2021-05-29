import sys
sys.stdin = open(file='data/49/27-49a.txt')
s = 0
ch, nech = 0, 0
min1 = 99999
min2 = 99999
for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    s += a
    if a % 2 == 0:
        ch += 1
    else:
        nech += 1
    r = b - a
    if r % 2 == 1 and min1 > r:
        min2 = min1
        min1 = r
    elif r % 2 == 1 and min2 > r:
        min2 = r
if s % 2 == 0 and nech == ch + 1 or s % 2 == 1 and nech == ch - 1:
    s += min1 + min2
elif s % 2 == 0 and ch < nech or s % 2 == 1 and nech < ch:
    s += min1
print(s)
