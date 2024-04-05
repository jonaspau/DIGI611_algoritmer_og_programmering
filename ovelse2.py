# Skriv en skript som ha litt interaksjon med brukeren (bruk print() og input() funksjoner og f-strenger)
# Sørg for at koden din fungerer ved å kjøre koden din.
# Skriv noen kommentarer om din første erfaring med Visual Studio Code og Python i denne diskusjonen nedenfor (trykk på svar knappen). Du kan også kopiere og lime inn koden din her slik at alle kan se flere eksempler.
# Skriv mer og mer komplisert kode. Lek med de forskjellige datatypene (heltall, ﬂyttall, streng)

# Pseudocode:
# Få gjennomføringsgrad fra brukeren
# Kontroller om score er over 60
# Gi tilbakemelding om bestått eller ikke

score = int(input("Fyll inn gjennomføringsgrad: "))
bestått = False

if score >= 60:
    bestått = True

if bestått == True:
    print(f"Gratulerer, med {score}% har du bestått!")
else:
    print(f"{score}% er dessverre ikke godt nok. Prøv igjen!")


# Versjon 2
score = int(input("Fyll inn gjennomføringsgrad: "))
bestått = False

if score >= 90:
    karakter = "A"
elif score >= 80:

if bestått == True:
    print(f"Gratulerer, med {score}% har du bestått!")
else:
    print(f"{score}% er dessverre ikke godt nok. Prøv igjen!")