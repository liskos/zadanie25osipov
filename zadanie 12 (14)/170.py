w = '5' + '6' * 120 + '5'
while '63' in w or '664' in w or '6665' in w:
    if '63' in w:
        w = w.replace('63', '4', 1)
    elif '664' in w:
        w = w.replace('664', '5', 1)
    elif '6665' in w:
        w = w.replace('6665', '663', 1)
print(w)
