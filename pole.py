predmety = ["Dějepis", "Biologie", "Zeměpis", "Matematika", "Český jazyk", "Chemie"]
print(len(predmety))
for i in predmety:
    print(i)
x = input("Další předmět")
predmety.append(x)
predmety.remove("Chemie")
predmety.sort()
print(predmety)
predmety.reverse()
print(predmety)