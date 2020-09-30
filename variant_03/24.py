file = open(file="Задание 24/24.txt", mode="r", encoding="utf8")
s = 0
for line in file:
    s += line.count("XYZ") + line.count("ZYX")
print(s)
file.close()
