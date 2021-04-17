k = 0
for i1 in range(1, 8):
    for i2 in range(8):
        for i3 in range(8):
            for i4 in range(8):
                for i5 in range(8):
                    for i6 in range(8):
                        for i7 in range(8):
                            if len({i1,i2,i3,i4,i5,i6,i7}) == 7 and i1 % 2 != i2 % 2 and i2 % 2 != i3 % 2 and i3 % 2 != i4 % 2 and i4 % 2 != i5 % 2 and i5 % 2 != i6 % 2 and i6 % 2 != i7 % 2:
                                k+=1
print(k)
