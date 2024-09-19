def multiplikator():
    tall_1 = float(input("Første tall: "))
    tall_2 = float(input("Andre tall: "))
    resultat = tall_1 * tall_2
    print(f"{tall_1} * {tall_2} = {resultat}")

    return(tall_1, tall_2, resultat)

tall_1, tall_2, resultat = multiplikator()