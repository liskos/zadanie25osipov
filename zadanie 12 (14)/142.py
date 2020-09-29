w = '2' * 282
while '222' in w or '6666' in w:
    if '222' in w:
        w = w.replace('222', '6', 1)
    else:
        w = w.replace('6666', '2', 1)
print(w)
