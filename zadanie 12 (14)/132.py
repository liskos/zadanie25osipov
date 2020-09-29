w = '8' * 125
while '333' in w or '888' in w:
    if '333' in w:
        w = w.replace('333', '8', 1)
    else:
        w = w.replace('888', '3', 1)
print(w)
