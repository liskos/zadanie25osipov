w = '4' * 186
while '4444' in w or '777' in w:
    if '4444'in w:
        w = w.replace('4444', '77', 1)
    else:
        w = w.replace('777', '4', 1)
print(w)
