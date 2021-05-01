import sys
sys.stdin = open(file='data/12/27-12b.txt')
n = int(input())
a6 = 0
a3 = 0
a2 = 0
a = 0
k = 0
for i in range(n):
    ch = int(input())
    if ch % 6 == 0:
        k += a + a2 + a3 + a6
        a6 += 1
    elif ch % 3 == 0:
        k += a2 + a6
        a3 += 1
    elif ch % 2 == 0:
        k += a3 + a6
        a2 += 1
    else:
        k += a6
        a += 1
print(k)