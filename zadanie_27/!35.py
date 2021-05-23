import sys
sys.stdin = open(file='data/35/27-35b.txt')
n = int(input())
a = []
s = ''
for i in range(n):
    ch = str(input())
    if ch != 0:
        s += ch
    else:
        a.append(s)
        s = ''
a.append(s)
b = [1, 1]
for s in a:
    chet = 0
    nech = 0
    for i in s:
        if int(i)%2 == 0:
            chet += 1
        else:
            nech += 1
    b[0] = b[0] * chet
    b[1] = b[1] * nech
print(sum(b))
