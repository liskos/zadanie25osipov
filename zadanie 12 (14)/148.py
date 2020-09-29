w = '4' * 123
while '4444' in w or '7777' in w:
    if '4444' in w:
        w = w.replace('4444', '77', 1)
    else:
        w = w.replace('7777', '44', 1)
print(w)
