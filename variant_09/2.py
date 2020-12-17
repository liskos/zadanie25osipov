for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            for w in (True, False):
                k = not y   # по каким-то причинам напрямую вписать не позволяет.
                f = (w or not x) and (w == k) and (not w or z)
                f = int(f)
                x = int(x)
                y = int(y)
                z = int(z)
                w = int(w)
                if f == 1:
                    print(x, y, z, w, '|', f)
