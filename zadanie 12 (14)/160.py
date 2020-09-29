w = '9' * 207
while '9999' in w or '333' in w:
    if '9999' in w:
        w = w.replace('9999', '3', 1)
    else:
        w = w.replace('333', '99', 1)
print(w)
