for a in (True, False):
    for b in (True, False):
        for c in (True, False):
            for d in (True, False):
                f = not (not b or a) and (not c or d) or a and d and c and not d
                f = int(f)
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                if f == 1:
                    print(a, b, c, d, '|', f)
