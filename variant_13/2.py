for a in True, False:
    for b in True, False:
        for c in True, False:
            f = a == (b or c) == b
            if f:
                f = int(f)
                a = int(a)
                b = int(b)
                c = int(c)
                print(a, b, c, '|', f)
