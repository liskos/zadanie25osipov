w = '8' * 93
while '222' in w or '888' in w:
    if '222' in w:
        w = w.replace('222', '8', 1)
    else:
        w = w.replace('888', '2', 1)
print(w)
