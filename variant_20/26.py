import sys
sys.stdin = open(file='Задание 26/26.txt')
s, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
s_a = 0
ma = 0
k = 0
for i in a:
    if s_a + i <= s:
        s_a += i
        ma = i
        k += 1
    else:
        break
print(k, '!',s,  s_a, ma, a)
