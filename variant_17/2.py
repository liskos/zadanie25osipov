for x in True, False:
    for y in True, False:
        for z in True, False:
            for w in True, False:
                f = not(x and y) and not(x == z) and w
                if f:
                    f = int(f)
                    x = int(x)
                    y = int(y)
                    z = int(z)
                    w = int(w)
                    print(x,y, z, w, '|', f)
