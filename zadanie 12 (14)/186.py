w = '7' * 170
while '777' in w:
    w = w.replace('777', '22', 1)
    w = w.replace('222', '7', 1)
print(w)
