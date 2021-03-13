for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = a == (b or c) == b
            if f:
                f = int(f)
                a = int(a)
                b = int(b)
                c = int(c)
                print(a, b, c, '|', f)
