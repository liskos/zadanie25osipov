for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = not x or y or w and not z
                if not f:
                    f = int(f)
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    print(w, y, z, x, '|', f)
