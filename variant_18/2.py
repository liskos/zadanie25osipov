for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = not (not (y or w) or (not x or z)) or (not x or w)
                if not f:
                    f = int(f)
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    print(x, y, z, w, '|', f)
