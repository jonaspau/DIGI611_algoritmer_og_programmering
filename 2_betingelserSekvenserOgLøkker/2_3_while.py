"""
Hovedmål: Be brukeren om å gi oss en karakter så lenge de ikke skriver -1.

Mer detaljert instruksjoner:
1. Opprett en tom liste
2. Opprett en variabel "karakter" som er et vilkårlig tall gitt at det
ikke er -1 (kan være f.eks. 0)
3. Bruk en while-løkke som fortsetter så lenge karakter != -1
4. I while-løkken: Skriv ut listen
5. I while-løkken: Be brukeren om å gi oss en karakter som blir lagret
i "karakter" variabelen (bruk input() og int() funksjoner)
6. I while-løkken: Bruk den på plass foranderlig sekvens metoden "append()" for
å legg til den nåværende karakteren på slutten av listen
7. (Valgfri) Fjern -1 fra slutten av listen (bruk de på plass foranderlig
sekvens metoder pop() eller remove())
8. (Valgfri) Etter løkken: Skriv ut listen
"""

# Tom liste til å lagre karakterer
karakterer = []

# En variabel med en vilkårlig karakter:
karakter = 0

# Loop for å legge inn karakterer:
while karakter != -1:
    print(f"Karakterliste: {karakterer}")
    karakter = int(input("Legg inn en karakter (-1 avslutter programmet): "))
    karakterer.append(karakter)

# Fjern -1 fra slutten av listen:
karakterer.pop()

print(f"Karakterer: {karakterer}")