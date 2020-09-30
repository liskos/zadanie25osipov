def algor(x):
    s = str(x)
    sum1 = int(s[0]) + int(s[1])
    sum2 = int(s[1]) + int(s[2])
    if sum1 > sum1:
        rez = str(sum1) + str(sum2)
    else:
        rez = str(sum2) + str(sum1)
    return int(rez)


for i in range(100, 1000):
    if algor(i) == 1712:
        print(i)
        break