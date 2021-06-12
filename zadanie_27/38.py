import sys

sys.stdin = open(file='data/38/27-38b.txt')
n = int(input())
a = [0] * 10
for _ in range(n):
    a[int(input())] += 1
if a[5] == 0:
    print(0)
elif a[5] == 1:
    print(5)
else:
    s = sum([a[i] // 2 * 2 * i for i in range(10)])
    r = max([a[i] % 2 * i for i in range(10)])
    print(s + r)
