a = []
x = 10
for i1 in range(3):
    if i1==0:
        x += 2
    if i1 == 1:
        x += 3
    if i1 == 2:
        x *= 2
    for i2 in range(3):
        if i2 == 0:
            x += 2
        if i2 == 1:
            x += 3
        if i2 == 2:
            x *= 2
        for i3 in range(3):
            if i3 == 0:
                x += 2
            if i3 == 1:
                x += 3
            if i3 == 2:
                x *= 2
            for i4 in range(3):
                if i4 == 0:
                    x += 2
                if i4 == 1:
                    x += 3
                if i4 == 2:
                    x *= 2
                for i5 in range(3):
                    if i5 == 0:
                        x += 2
                    if i5 == 1:
                        x += 3
                    if i5 == 2:
                        x *= 2
                    a.append(x)
    x = 10
b = set(a)
print(len(b))
