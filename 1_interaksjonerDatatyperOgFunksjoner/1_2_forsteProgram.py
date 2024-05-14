# Pseudocode:
# Få gjennomføringsgrad fra brukeren
# Kontroller om score er over 60
# Gi tilbakemelding om bestått eller ikke

# Script:

score = int(input("Fyll inn gjennomføringsgrad: "))
bestått = False

if score >= 60:
    bestått = True

if bestått == True:
    print(f"Gratulerer, med {score}% har du bestått!")
else:
    print(f"{score}% er dessverre ikke godt nok. Prøv igjen!")
