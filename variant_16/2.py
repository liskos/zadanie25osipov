for x in True, False:
    for y in True, False:
        for z in True, False:
            for w in True, False:
                f = not(x or y) or (x == z) or not w
                if not f:
                    f = 0
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    print(x, w, z, y, '|', f)
