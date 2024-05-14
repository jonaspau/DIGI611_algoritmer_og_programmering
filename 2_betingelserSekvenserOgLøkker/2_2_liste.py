"""
1. Skriv ut hvor mange elementer det er i listen (len() og print() funksjoner)
2. Skriv ut den første karakteren i listen (indeksering og print())
3. Skriv ut om det forekommer karakteren 0 i listen ("in" operator og print())
4. Spør brukeren om å angi en ny karakter (input())
5. Legg til karakteren på slutten av listen (bruk den på plass foranderlig
sekvens metoden "append()")
6. Skriv ut listen (print())
"""

karakterer = [3, 4, 5, 6, 8, 12, 10]

karakterer_lengde = len(karakterer)
print(F"Karakterer har {karakterer_lengde} elementer: {karakterer}")

print(f"{karakterer[0]} er første karakter.")

if 0 in karakterer:
    print("0 er blant karakterene")
else:
    print("0 er ikke blant karakterene, hurra!")

ny_karakter = int(input("Legg til en karakter: "))
karakterer.append(ny_karakter)

print(karakterer)