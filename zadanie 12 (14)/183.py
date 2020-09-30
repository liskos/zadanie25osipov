w = '1' * 198
while '1111' in w:
        w = w.replace('1111', '33', 1)
        w = w.replace('333', '1', 1)
print(w)
