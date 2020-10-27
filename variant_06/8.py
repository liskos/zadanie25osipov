k = 0
for a1 in "ЗАПИС":
    for a2 in "ЗАПИСЬ":
        for a3 in "ЗАПИСЬ":
            for a4 in "ЗАПИСЬ":
                for a5 in "ЗАПИСЬ":
                    for a6 in "ЗАПИСЬ":
                        a = set(a1 + a2 + a3 + a4 + a5 + a6)
                        if len(a) == 6: k += 1
print(k)
