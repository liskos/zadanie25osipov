def kol(och):
    chet, nech, chet_13, nech_13 = 0, 0, 0, 0
    for i in och:
        if i % 2 == 0 and i % 13 == 0:
            chet_13 += 1
        elif i % 2 == 1 and i % 13 == 0:
            nech_13 += 1
        elif i % 2 == 0 and i % 13 != 0:
            chet += 1
        else:
            nech += 1
    return chet, nech, chet_13, nech_13


import sys
sys.stdin = open(file='data/18/27-18b.txt')
n = int(input())
k = 0
och = [int(input()) for _ in range(4)]
for i in range(4, n):
    a = int(input())
    chet, nech, chet_13, nech_13 = kol(och)
    if a % 2 == 0 and a % 13 == 0:
        k += nech + nech_13
    elif a % 2 == 1 and a % 13 == 0:
        k += chet + chet_13
    elif a % 2 == 0 and a % 13 != 0:
        k += nech_13
    else:
        k += chet_13
    och.pop(0)
    och.append(a)
print(k)
