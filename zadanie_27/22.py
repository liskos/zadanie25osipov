import sys
sys.stdin = open(file='data/22/27-22a.txt')
n = int(input())
s = 0
r = [10001] * 10
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += a
    for i in range(10):
        r[(b-a+i)%10] = min(r[(b-a+i)%10], r[i] + b - a)
    r[(b - a) % 10] = min(r[(b - a) % 10], b - a)
if s % 10 != 4:
    s = s + r[(4 - s)%10]
print(s)
