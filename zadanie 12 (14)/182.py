w = '5' * 150
while '5555' in w:
        w = w.replace('5555', '33', 1)
        w = w.replace('333', '5', 1)
print(w)
