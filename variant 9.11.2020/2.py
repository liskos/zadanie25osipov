for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = (not x or z) and (not z or w) or (y == (x or y))
                if not f:
                    f, x, y, z, w = int(f), int(x), int(y), int(z), int(w)
                    print(x, y, z, w, '|', f)
#таблица не соответствует