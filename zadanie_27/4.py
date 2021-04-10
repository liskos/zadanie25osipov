import sys
sys.stdin = open(file='data/4/27-4b.txt')
n = int(input())
s = 0
min_r1a = 9999
min_r1b = 9999
min_r1c = 9999
min_r1d = 9999
min_r2a = 9999
min_r2b = 9999
min_r3 = 9999
min_r4 = 9999
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a - b)
    if r % 5 == 4 and r > min_r4:
        min_r4 = r
    elif r % 5 == 3 and min_r3 > r:
        min_r3 = r
    elif r % 5 == 2:
        if r < min_r2a:
            min_r2b = min_r2a
            min_r2a = r
        elif r < min_r2b:
            min_r2b = r
    elif r % 5 == 1:
        if r < min_r1a:
            min_r1d = min_r1c
            min_r1c = min_r1b
            min_r1b = min_r1a
            min_r1a = r
        elif r < min_r1b:
            min_r1d = min_r1c
            min_r1c = min_r1b
            min_r1b = r
        elif r < min_r1c:
            min_r1d = min_r1c
            min_r1c = r
        elif r < min_r1d:
            min_r1d = r
if s% 5 == 1:
    s -= min_r1a
elif s%5 == 2:
    s -= min(min_r2a, (min_r1a + min_r1b))
elif s % 5 == 3:
    s -= min(min_r3, (min_r2a + min_r1a), (min_r1a + min_r1b + min_r1c))
elif s % 5 == 4:
    s -= min(min_r4, (min_r3 + min_r1a), (min_r2a + min_r1a + min_r1b), (min_r2a + min_r2b), (min_r1a + min_r1b + min_r1c + min_r1d))
print(s)