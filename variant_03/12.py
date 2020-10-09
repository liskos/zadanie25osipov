w = '3' * 95
while '333' in w or '999' in w:
    if '999' in w:
        w = w.replace('999', '3', 1)
    else:
        w = w.replace('333', '9', 1)
print(w)
