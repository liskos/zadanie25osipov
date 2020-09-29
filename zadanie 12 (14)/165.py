w = '3' + '5' * 100
while '25' in w or '355' in w or '4555' in w:
    if '25' in w :
        w = w.replace('25', '4', 1)
    if '355' in w:
        w = w.replace('355', '2', 1)
    if '4555' in w:
        w = w.replace('4555', '3', 1)
print(w)
