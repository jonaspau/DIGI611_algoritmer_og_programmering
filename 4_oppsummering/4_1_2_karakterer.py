"""
Vi antar at vi har en students karakterer lagret i en ordbok. Denne ordboken består da av fag-karakterer par.

Oppgave 1: Skriv en funksjon som beregner gjennomsnittskarakteren til en student.
Hint: Vi har allerede løst en oppgave som beregner dette når karakterene var lagret i en liste. Vi må nå tilpasse denne løsningen til en ordbok.

Oppgave 2: Skriv en annen funksjon som returnerer faget der studenten har den beste karakteren. Det vil si at vi må finne den beste karakteren, og det tilhørende faget.
Hint: Vi har allerede løst en oppgave som finner maksimum i en liste med kun positive tall. Vi må nå tilpasse denne løsningen til en ordbok, og i tillegg må vi lagre faget som samsvarer med den beste karakteren.
"""

ordbok_karakterer = {
    "Matematikk" : 12,
    "Historie": 15,
    "Kemi": 19,
    "Informatikk": 16,
    "Litteratur": 8,
}

def gjsn_kar(karakterer):
    total_sum = 0
    for fag, karakter in karakterer.items():
        total_sum = total_sum + karakter
    antall_fag = len(karakterer)
    gjennomsnitt = total_sum / antall_fag

    return(gjennomsnitt)


def høy_kar(karakterer):
    best_kar = 0

    for fag, karakter in karakterer.items():
        if karakter > best_kar:
            best_kar = karakter
            best_fag = fag

    return(best_kar, best_fag)
    

gjennomsnitt = gjsn_kar(ordbok_karakterer)
print(gjennomsnitt)

beste_fag, høyeste_karakter = høy_kar(ordbok_karakterer)
print(beste_fag, høyeste_karakter)
