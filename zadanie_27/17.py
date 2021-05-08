import sys
sys.stdin = open(file='data/17/27-17a.txt')
n = int(input())
chet, nech, chet_13, nech_13 = 0, 0, 0, 0
och = [int(input()) for _ in range(5)]
k = 0
for i in range(5, n):
    a = int(input())
    if och[0] % 2 == 0 and och[0] % 13 == 0:
        chet_13 += 1
    elif och[0] % 2 == 1 and och[0] % 13 == 0:
        nech_13 += 1
    elif och[0] % 2 == 0 and och[0] % 13 != 0:
        chet += 1
    else:
        nech += 1

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
