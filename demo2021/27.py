import sys
sys.stdin = open(file='Задание 27/27-B.txt')
k = int(input())
razn = 9999
s = 0
for i in range(k):
    a, b = map(int, input().split())
    s += max(a, b)
    razn1 = max(a, b) - min(a, b)
    if razn > razn1 and razn1 % 3 !=0:
        razn = razn1
if s % 3 != 0:
    print(s)
else:
    print(s - razn)
