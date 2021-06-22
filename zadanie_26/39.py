import sys
sys.stdin = open(file='26data/26-39.txt')
n, m = map(int, input().split())
a, b = [], []
s, k, nom = 0, 0, 0
for _ in range(n):
    ch = int(input())
    if 180 <= ch <= 200:
        a.append(ch)
    else:
        b.append(ch)
b.sort()
a.sort(reverse=True)
for i in range(len(a)):
    if a[i] + s <= m:
        s += a[i]
        k += 1
for i in range(len(b)):
    if b[i] + s <= m:
        s += b[i]
        k += 1
        nom = i
b.sort(reverse=True)
s_safe = s
last_s = s
while not(s == m) and nom > 0 and last_s <= s:
    last_s = s
    s -= b[nom]
    for i in range(len(b)):
        if b[i] + s <= m:
            s += b[i]
            b.pop(i)
    nom -= 1
if s >= last_s >= s_safe:
    print(k, s)
elif last_s >= s_safe:
    print(k, last_s)
else:
    print(k, s_safe)
