import sys
sys.stdin = open(file='data/21/27-21a.txt')
n = int(input())
r = [10001 for i in range(10)]
s = 0
for i in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    for i in range(10):
        r[(b-a+i)%10] = min(r[(b-a+i)%10], r[i] + b - a)
    r[(b-a)%10] = min(r[(b-a)%10], b-a)
if s % 10 != 8:
    s = s - r[(s - 8)%10]
print(s)

