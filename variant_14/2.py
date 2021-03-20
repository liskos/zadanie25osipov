for x in True,False:
    for y in True, False:
        for z in True, False:
            for w in True, False:
                f = (x and not y) or (y == z) or not w
                if not f :
                    f = int(f)
                    z = int(z)
                    y = int(y)
                    x = int(x)
                    w = int(w)
                    print(x, y, z, w, '|', f)
