import sys
sys.stdin = open(file='26-s1.txt')
n = int(input())
s = 0
a = []
for i in range(n):
    c = int(input())
    if c <= 150:
        s += c
    else:
        a.append(c)
a.sort()
print(a[len(a)//2])
for i in range(len(a)//2):
    a[i] = a[i] * 0.8
print(s + sum(a))