import sys
sys.stdin = open(file='data/15/27-15a.txt')
n = int(input())
k = [0 for _ in range(14)]
ocher = [int(input()) for _ in range(5)]
s = 0
for i in range(5, n):
    ocher.append(int(input()))
    k[ocher[0] % 14] += 1
    ocher.pop(0)
    s += k[- ocher[-1] % 14]
print(s)
