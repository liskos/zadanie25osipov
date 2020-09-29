w = '3' + '6' * 115 + '3'
while '63' in w or '664' in w or '6665' in w:
    if '63' in w:
        w = w.replace('63', '4', 1)
    elif '664' in w:
        w = w.replace('664', '65', 1)
    elif '6665' in w:
        w = w.replace('6665', '63', 1)
print(w)
