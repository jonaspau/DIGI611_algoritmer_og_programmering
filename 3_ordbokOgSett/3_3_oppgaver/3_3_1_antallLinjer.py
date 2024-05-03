with open("Askeladden_og_de_gode_hjelperne.txt", mode="tr") as f:
    linjer = f.read().split("\n")

print(f"Antall linjer: {len(linjer)}")