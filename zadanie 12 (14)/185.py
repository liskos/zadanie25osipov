w = '2' * 103
while '222' in w:
    w = w.replace('22', '7', 1)
    w = w.replace('77', '2', 1)
print(w)
