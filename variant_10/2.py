for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            for w in (True, False):
                f = (not x and not y) or (y == z) or not w
                f = int(f)
                x = int(x)
                y = int(y)
                z = int(z)
                w = int(w)
                if f == 0:
                    print(x, y, z, w, '|', f)
