import sys
sys.stdin = open(file='26data/26-j9.txt')
v, n = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
min_ch = a[:n//2]
max_ch = a[n//2:]
max_ch.sort(reverse=True)
k, last, s, nom_max = 0, 0, 0, 0
for _ in range(n//2):
    for i in range(nom_max, n//2):
        if k % 2 == 0 and s + max_ch[i] <= v:
            k += 1
            s += max_ch[i]
            last = max_ch[i]
            nom_max = i
            break
    for i in range(k//2, n//2):
        if k % 2 == 1 and s + min_ch[i] <= v:
            k += 1
            s += min_ch[i]
            last = min_ch[i]
print(k, last)
