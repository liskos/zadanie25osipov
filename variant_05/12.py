a = '>' + 15 * '1' + 20 * '2' + 25 * '3'
if '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a = a.replace('>1', '22>', 1)
    if '>2' in a:
        a = a.replace('>2', '2>1', 1)
    if '>1' in a:
        a = a.replace('>3', '1>', 1)
q = []
q = map(int, a.replace('>', ''))
print(sum(q))
