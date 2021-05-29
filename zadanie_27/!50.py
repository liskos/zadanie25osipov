import sys
sys.stdin = open(file='data/50/27-50b.txt')
s = 0
ch, nech = 0, 0
min1ch = 99999
min2ch = 99999
min1ne = 99999
min2ne = 99999
for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    s += b
    if a % 2 == 0:
        ch += 1
    else:
        nech += 1
    r = b - a
    if r % 2 == 1 and min1ne > r and a % 2 == 1:
        min2ne = min1ne
        min1ne = r
    elif r % 2 == 1 and min1ch > r and a % 2 == 0:
        min2ch = min1ch
        min1ch = r
    elif r % 2 == 1 and min2ne > r and a % 2 == 1:
        min2ne = r
    elif r % 2 == 1 and min2ch > r and a % 2 == 0:
        min2ch = r
#if s % 2 == 0 and nech == ch + 1:
#    s += min1ch + min2ch
#elif s % 2 == 1 and nech == ch - 1:
#    s += min1ne + min2ne
if s % 2 == 1 and ch < nech:
    s += min1ch
elif s % 2 == 0 and nech < ch:
    s += min1ne
print(s)
