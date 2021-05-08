import sys
sys.stdin = open(file='data/16/27-16a.txt')
n = int(input())
chet, nech, chet_13, nech_13 = 0, 0, 0, 0
k = 0
for i in range(n):
    a = int(input())
    if a % 2 == 0 and a % 13 == 0:
        k += nech + nech_13
        chet_13 += 1
    elif a % 2 == 1 and a % 13 == 0:
        k += chet + chet_13
        nech_13 += 1
    elif a % 2 == 0 and a % 13 != 0:
        k += nech_13
        chet += 1
    else:
        k += chet_13
        nech += 1
print(k)
