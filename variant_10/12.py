a = '1' + '0' * 55
while '10' in a or '1' in a:
    if '10' in a:
        a = a.replace('10', '001', 1)
    else:
        if '1' in a:
            a = a.replace('1', '0', 1)
print(a.count('0'))
