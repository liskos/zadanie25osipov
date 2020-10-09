def al(s):
    a = list(map(int, str(s)))
    little, big = min(a[0]+a[1], a[1]+a[2]), max(a[0]+a[1], a[1]+a[2])
    return int(str(big) + str(little))


for i in range(100, 1000):
    if al(i) == 1712:
        print(i)
        break
