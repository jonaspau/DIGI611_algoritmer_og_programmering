def sjekk_alder(a):
    if a >= 18:
        print("Voksen")
    elif a >= 0:
        print("Barn")
    else:
        print("Alder kan ikke vøre minder enn 0")

alder = int(input("Hvor gammel er du? "))

sjekk_alder(alder)