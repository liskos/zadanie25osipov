import sys
sys.stdin = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
s1 = int(0.7 * sum(a[:int(0.7*n)]) + 0.6 * sum(a[int(0.7*n):])) #1variant
s2 = int(0.6 * sum(a[:int(0.5*n)]) + 0.65 * sum(a[int(0.5*n):])) #2variant
if s1 > s2:
    print(s1 - s2, 0.6 * max(a))
else:
    print(s2 - s1, 0.65 * max(a))
