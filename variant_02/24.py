import sys

file = open(file="Задание 24/24.txt", mode="r", encoding="utf8")
sys.stdin = file

for s in file:
    print(s.count("TOK") + s.count("TIK"))
