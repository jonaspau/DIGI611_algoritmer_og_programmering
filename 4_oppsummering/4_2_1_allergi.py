"""
Oppgave: Skriv en funksjon som:
- tar som parameter en liste over alle matrestriksjonene til deltakerne på et
arrangement, og en streng som representeres en gitt allergi (som for eksempel "nøtter")
- og beregner og returnerer antall personer som har denne spesifikke
matrestriksjonen. Det vil si en funksjon som beregner antall
forekomster av denne restriksjonen i listen.
Hint:
- En for løkke og en if setning kan være nyttige her.
"""

# En list over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "gluten",  "fisk", "laktose", "gluten", "kjøtt",
    "nøtter", "melk", "svinn", "svinn", "egg",
    "laktose", "fisk", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "gluten", "gluten", "kjøtt",
    "kjøtt"
]

restriksjon = "nøtter"

def allergi_antall(allergi, allergier):
    antall = 0

    for i in allergier:
        if i == allergi:
            antall = antall + 1
    return(antall)


antall_personer = allergi_antall(restriksjon, mat_restriksjoner)

print(f"Antall personer som har allergi mot {restriksjon}: {antall_personer}")
