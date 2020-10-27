s = '>' + 20 * '0' + 30 * '1'
while '>1' in s or '>0' in s:
    if '>10' in s:
        s = s.replace('>10', '3>', 1)
    else:
        if '>0' in s:
            s = s.replace('>0', '2>', 1)
        if '>1' in s:
            s = s.replace('>1', '0>0', 1)
s = sum(map(int, s.replace('>', '')))
print(s)
