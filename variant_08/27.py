import sys
file = open(file='Задание 27/27-B.txt', mode='r', encoding='utf8')
sys.stdin = file
n = int(input())
a = []
b = []
s = 0
a.append(10001)
b.append(10001)
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        a.append(k)
        if k > min(b):
            s += len(b) - 1
    else:
        b.append(k)
        if k > min(a):
            s += len(a) - 1
print(s)
