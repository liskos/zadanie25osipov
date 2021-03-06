a = 'AB' * 52
while 'AA' in a or 'BB' in a or 'AB' in a:
    a = a.replace('AA', 'B', 1)
    a = a.replace('BB', 'A', 1)
    a = a.replace('AB', 'BA', 1)
print(a)
