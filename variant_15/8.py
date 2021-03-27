#6-10
k6 = 0
for i1 in '13579':
    for i2 in '02468':
        for i3 in '13579':
            for i4 in '02468':
                for i5 in '13579':
                    for i6 in '02468':
                        k6 += 1
for i1 in '2468':
    for i2 in '13579':
        for i3 in '02468':
            for i4 in '13579':
                for i5 in '02468':
                    for i6 in '13579':
                        k6 += 1
print(k6-6561)
