import sys
sys.stdin = open(file='data/21/27-21a.txt')
n = int(input())
minr1 = [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]
minr2 = [9999, 9999, 9999, 9999]
minr3 = [9999, 9999, 9999]
minr4 = [9999, 9999]
minr5 = 9999
minr6 = 9999
minr7 = 9999
minr8 = 9999
minr9 = 9999
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a - b)
    if r % 10 == 1 and r < minr1[8]:
        minr1.append(r)
        minr1.sort()
        minr1.pop(9)
    elif r % 10 == 2 and r < minr2[3]:
        minr2.append(r)
        minr2.sort()
        minr2.pop(4)
    elif r % 10 == 3 and r < minr3[2]:
        minr3.append(r)
        minr3.sort()
        minr3.pop(3)
    elif r % 10 == 4 and r < minr4[1]:
        minr4.append(r)
        minr4.sort()
        minr4.pop(2)
    elif r % 10 == 5 and r < minr5:
        minr5 = r
    elif r % 10 == 6 and r < minr6:
        minr6 = r
    elif r % 10 == 7 and r < minr7:
        minr7 = r
    elif r % 10 == 8 and r < minr8:
        minr8 = r
    elif r % 10 == 9 and r < minr9:
        minr9 = r
if s % 10 == 0:
    s -= min(minr2[0], (minr1[0] + minr1[1]))
elif s % 10 == 1:
    s -= min(minr3[0], (minr1[0] + minr2[0]), (minr1[0] + minr1[1] + minr1[2]))
elif s % 10 == 2:
    s -= min(minr4[0], (minr2[0] + minr2[1]), (minr3[0] + minr1[0]), sum(minr1[0:4]))
elif s % 10 == 3:
    s -= min(minr5, (minr4[0] + minr1[0]), (minr3[0], minr2[0]), sum(minr1[0], minr2[0:2]), sum(minr1[0:5]))
elif s % 10 == 4:
    s -= min(minr6, (minr5 + minr1[0]), (minr4 + min(minr2[0], (minr1[0] + minr1[1]))), (minr3[0] + min(minr3[1], (minr1[0], minr2[0]), sum(minr1[0:3]))), sum(minr1[0:6]))
elif s % 10 == 5:
    s -= min(minr7, (minr6 + minr1[0]), (minr5 + min(minr2[0], (minr1[0] + minr1[1])), (minr4[0] + min(minr3[0], (minr2[0], minr1[0]), sum(minr2[0:2], min(minr3[0], (minr2[0] + minr1[0]), sum(minr1[0:3])))))), sum(minr1[0:7]))
elif s % 10 == 6:
    s -= min(minr8, (minr7 + minr1[0]), (minr6 + min(minr2[0], (minr1[0] + minr1[1])), (minr5[0] + min(minr3[1], (minr2[0], minr1[0]), sum(minr1[0:3])))), sum(minr4[0], min(minr4[1], (minr3[0] + minr1[0]), sum(minr2[0:2]), sum(minr1[0:5]))), sum(minr1[0:9]))
elif s % 10 == 7:
    s -= min(minr9, (minr8 + minr1[0]), (minr7 + min(minr2[0], (minr1[0] + minr1[1])), (minr6[0] + min(minr3[1], (minr2[0], minr1[0]), sum(minr1[0:3])))), sum(minr5[0], min(minr4[0], (minr3 + minr1), sum(minr2[0:2]), sum(minr1[0:5]))), sum(minr4[0] + min((minr4[1] + minr1(0)), sum(minr3[0], min(minr2[0], (minr1[0] + minr1[1]))), sum(minr1[0:5]))), sum(minr3[0], minr3[1], min(minr3[2], (minr2[0] + minr1[0]))), sum(minr1))
elif s % 10 == 9:
    s -= minr1[0]
elif s % 10 == 0:
    s -= min(minr2[0], (minr1[0] + minr1[1]))
print(s)
##########