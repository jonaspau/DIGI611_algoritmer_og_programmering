"""
1. Spør brukeren om navnet deres (input() funksjonen)
2. Beregn hvor mange bokstaver det er i navnet deres (len() sekvens funksjonen)
3. Skriv ut hvor mange bokstaver det er i navnet deres (print() funksjonen)
4. Hent ut den første bokstaven i navnet deres (bruk sekvens indeksering)
5. Skriv ut den første bokstaven i navnet deres (print() funksjonen)
6. Sjekk om det forekommer bokstaven "a" i navnet deres (bruk "in" sekvens operator)
7. Skriv ut om det forekommer bokstaven "a" i navnet deres (print() funksjonen)
"""

navn = input("Hei, hva heter du? ")
navn_lengde = len(navn)
print(f"{navn} har {navn_lengde} bokstaver.")

første_bokstav = navn[0]
print(f"{første_bokstav} er første bokstav i {navn}.")

har_a = False
if "a" in navn:
    har_a = True
    print(f"{navn} har a i navnet. Flaks :)")
else:
    print(f"{navn} har ikke a i navnet. Så synd :(")
    

