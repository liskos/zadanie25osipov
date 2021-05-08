import sys
sys.stdin = open(file='data/13/27-13b.txt')
n = int(input())
a14 = 0
a7 = 0
a2 = 0
a = 0
ocher = [int(input()) for i in range(7)]
k = 0
for i in range(n-7):
    ch = int(input())
    if ocher[0] % 14 == 0:
        a14 += 1
    elif ocher[0] % 7 == 0:
        a7 += 1
    elif ocher[0] % 2 == 0:
        a2 += 1
    else:
        a += 1
    ocher.append(ch)
    if ch % 14 == 0:
        k += a + a2 + a7 + a14
    elif ch % 7 == 0:
        k += a2 + a14
    elif ch % 2 == 0:
        k += a7 + a14
    else:
        k += a14
    ocher.pop(0)
print(k)