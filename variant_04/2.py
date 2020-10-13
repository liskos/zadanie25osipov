for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            f = (not x or y) and (not y or z)
            print(int(x), int(y), int(z), "|", int(f))
print("----------")
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            f = (not x or y) and (not y or z)
            if f and (not (x and y and z)) and (x or y or z):
                print(int(z), int(x), int(y), "|", int(f))