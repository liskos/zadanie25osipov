for a in True,False:
    for b in True, False:
        for c in True, False:
            f = a == (not b or c)
            if f:
                a = int(a)
                b = int(b)
                c = int(c)
                f = int(f)
                print(a,b,c,'|', f)