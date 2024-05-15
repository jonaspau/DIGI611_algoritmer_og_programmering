import matplotlib.pyplot as plt

with open("allergier.txt", mode="rt") as f:
    linjer = f.read().split("\n")

# Lag en liste over navn og allergier:
navn_og_allergier = {}

for l in linjer:
    # fiks skrivefeil i originalt datasett
    l = l.replace("svinn", "svin")

    # splitt dataene i navn og allergier:
    delt = l.split(":")

    navn = delt[0]
    allergier_str = delt[1]
    # Splitt allergiene fra en streng til en liste:
    allergier_liste = allergier_str.split(", ")

    navn_og_allergier[navn] = allergier_liste

print(navn_og_allergier)

# Lag en graf som viser antall allergier:
allergier = []

for l in linjer:
    # fiks skrivefeil i originalt datasett
    l = l.replace("svinn", "svin")
    delt = l.split(":")

    allergier_str = delt[1]
    allergier_liste = allergier_str.split(", ")

    allergier = allergier + allergier_liste

def allergiteller(allergiliste):
    allergier = {}

    for allergi in allergiliste:
        if allergi in allergier:
            allergier[allergi] = allergier[allergi] +1
        else:
            allergier[allergi] = 1
    
    return allergier

allergioversikt = allergiteller(allergier)

print(allergioversikt)

fig, ax = plt.subplots()

ax.bar(x=list(allergioversikt.keys()), height=allergioversikt.values())
ax.set_title("Antall allergier")
ax.set_xlabel("Allergi")
ax.set_ylabel("Antall")

plt.show()