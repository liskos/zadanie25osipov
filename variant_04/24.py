file = open(file="Задание 24/24.txt", mode="r", encoding="utf8")
boss = 0
jboss = 0
jbossj = 0
bossj = 0
for line in file:
    boss += line.count("BOSS")
    bossj += line.count("BOSSJ")
    jboss += line.count("JBOSS")
    jbossj += line.count("JBOSSJ")
print(boss - (bossj + jboss - jbossj))
