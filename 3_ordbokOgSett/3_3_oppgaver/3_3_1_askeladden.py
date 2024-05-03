with open("Askeladden_og_de_gode_hjelperne.txt", mode="tr") as f:
    linjer = f.read().split("\n")


#Tell antall linjer
print("\nOpg2: tell antall linjer: \n")
ant_linjer = len(linjer)
print(ant_linjer)

#Skriv ut alle linjer som inneholder Askeladden, og linjen før
print("\nOpg 3: Skriv ut Alle linjer som innheolder Askeladden, og linjen før:\n")
for i in range(ant_linjer):
    if "Askeladden" in linjer[i]:
        print(linjer[i-1])
        print(linjer[i])

# Skriv ut alle linjer som innheolder ASkeladden, men bytt med Jonas

print("\nOpg 4: Erstatt med eget navn:\n")
for i in range(ant_linjer):
    if "Askeladden" in linjer[i]:
        print(linjer[i-1])
        print(linjer[i].replace("Askeladden", "Jonas"))

