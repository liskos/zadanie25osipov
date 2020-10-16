for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            for w in [False, True]:
                f = (x or not y) and (not(x == z)) and w
                print(int(x), int(y), int(z), int(w), int(f))
print("-------------")
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            for w in [False, True]:
                f = (x or not y) and (not(x == z)) and w
                if f:
                    print(int(w), int(z), int(y), int(x), int(f))
