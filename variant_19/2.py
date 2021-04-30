for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = ((not y or x) or (not z and w)) == (w == x)
                if f:
                    f = int(f)
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    print(x, y, z, w, '|', f)
