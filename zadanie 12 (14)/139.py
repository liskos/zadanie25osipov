w = '6' * 166
while '2222' in w or '666' in w:
    if '2222' in w:
        w = w.replace('2222', '6', 1)
    else:
        w = w.replace('666', '2', 1)
print(w)
