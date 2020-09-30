w = '5' * 400
while '555' in w or '333' in w:
    if '555' in w:
        w = w.replace('555', '3', 1)
    else:
        w = w.replace('333', '5', 1)
print(w)
