for x in True, False:
    for y in True, False:
        for z in True, False:
            for w in True, False:
                f = not (x or y) or (y == z) or w
                if not f:
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    f = int(f)
                    print(x, y, y, w, '|', f)
