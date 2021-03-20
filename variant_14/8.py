k = 0
for i1 in '2468acf':
    for i2 in '13579bd':
        for i3 in '02468acf':
            for i4 in '13579bd':
                k+=1
for i1 in '13579bd':
    for i2 in '02468acf':
        for i3 in '13579bd':
            for i4 in '02468acf':
                k += 1
print(k)