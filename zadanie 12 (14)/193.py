w = '7' * 120
while '88777' in w or '7' in w:
    if '88777' in w:
        w = w.replace('88777', '7', 1)
    else:
        w = w.replace('7', '8', 1)
print(w)
