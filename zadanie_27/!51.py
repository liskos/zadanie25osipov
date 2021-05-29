import sys
sys.stdin = open(file='data/51/27-51b.txt')
s = 0
ch, nech = 0, 0
min1ch = 99999
min1ne = 99999
for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    s += a
    if a % 2 == 0:
        ch += 1
    else:
        nech += 1
    r = b - a
    if r % 2 == 1 and min1ne > r and b % 2 == 1:
        min1ne = r
    elif r % 2 == 1 and min1ch > r and b % 2 == 0:
        min1ch = r
if s % 2 == 1 and ch < nech:
    s += min1ch
elif s % 2 == 0 and nech < ch:
    s += min1ne
print(s)
