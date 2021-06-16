def func(x, y):
    global r
    if (x, y) in r:
        return r[x, y]
    if x + y >= 63:
        return 0
    ans = [(x + 1, y), (x, y+1), (x*2, y), (x, y*2)]
    if func(*ans[0])*func(*ans[1])*func(*ans[2])*func(*ans[3]) == 0:
        return 1
    if func(*ans[0])==func(*ans[1])==func(*ans[2])==func(*ans[3]) == 1:
        return 2
    z = [func(*ans[0]), func(*ans[1]), func(*ans[2]), func(*ans[3])]
    if 0 in set(z) or 2 in set(z):
        return 3
    if set(z) <= {1, 3}:
        return 4

    return 5





r = dict([])
for y in range(90, 0, -1):
    for x in range(90, 0, -1):
        r[(x, y)] = func(x, y)
for y in range(1, 91):
    for x in range(1, 91):
        print(r[(x, y)], end="\t")
    print()
