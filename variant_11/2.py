for x in True, False:
    for y in True, False:
        for z in True, False:
            for w in True, False:
                f = ((not x) + (not y)) and not (y == z) and not w
                f = int(f)
                x = int(x)
                y = int(y)
                z = int(z)
                w = int(w)
                if f == 1:
                    print(x, y, z, w, '|', f)