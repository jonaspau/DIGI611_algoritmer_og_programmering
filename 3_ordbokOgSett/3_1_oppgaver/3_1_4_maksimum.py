"""
Oppgave: Finn maksimum i en liste med kun positive tall
En for løkke og en if setning kan være nyttig her
"""

l = [2, 1, 36, 12, 4, 2, 4, 46, 59, 10, 0]

max = 0

for i in l:
    if i > max:
        max = i

print(f"{max} er den høyeste verdien")