import sys
sys.stdin = open(file='data/13/27-13b.txt')
n = int(input())
a14 = 0
a7 = 0
a2 = 0
a = 0
k = 0
for i in range(n):
    ch = int(input())
    if ch % 14 == 0:
        k += a + a2 + a7 + a14
        a14 += 1
    elif ch % 7 == 0:
        k += a2 + a14
        a7 += 1
    elif ch % 2 == 0:
        k += a7 + a14
        a2 += 1
    else:
        k += a14
        a += 1
print(k)