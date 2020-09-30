w = '7' * 170
while '777' in w:
    w = w.replace('77', '2', 1)
    w = w.replace('22', '7', 1)
print(w)
