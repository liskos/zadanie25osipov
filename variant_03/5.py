for i in range(100, 1000):
    i = str(i)
    x1, x2, x3 = map(int, i)
    y1, y2 = x1 + x2, x2 + x3
    s1, s2 = str(y1), str(y2)
    if y1 > y2:
        s = s1 + s2
    else:
        s = s2 + s1
    if s == '1712':
        print(i)
        break
