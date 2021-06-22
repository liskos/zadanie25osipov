import sys
sys.stdin = open(file='26data/26-k6.txt')
n, k = map(int, input().split())
k_used = 0
s = [0, 0]
p = []
for i in range(n):
    a, b = map(int, input().split())
    p.append([a, b])
p.sort(key=lambda x: x[1], reverse=True)
p.sort(key=lambda x: x[0])
for i in range(n):
    if k_used < k:
        s[0] += p[i][0]
        s[1] += p[i][1]
        k_used += 1
    else:
        break
print(s[1])
print(max(p[:k], key= lambda x: x[1])[0])
