"""
Hovedmål: Opprett en ordnet liste av tall, mellom to tall (for eks. 50 og 100)
e.g [50, 51, 52, ..., 98, 99, 100]

Mer detaljert instruksjoner:
1. Opprett en tom liste
2. Bruk en for-løkke med range() for å iterere over tallene mellom 50 og 100
3. I for-løkken: bruk den på plass foranderlig sekvens metoden "append()" for å
legg til den nåværende tallet på slutten av listen
4. Etter løkken: skriv ut listen
"""

# Tom liste
tall = []

# For loop som legger til i+50 51 ganger:
for i in range(51):
    tall.append(i + 50)

print(tall)