# Importerer biblioteket vi trenger og gir det et navn (plt)
import matplotlib.pyplot as plt

# En liste over allergier:
mat_restriksjoner = [
"egg", "nøtter", "kjøtt", "svin", "fisk",
"laktose", "fisk", "laktose", "kjøtt", "laktose", "kjøtt",
"nøtter", "melk", "svin", "egg", "nøtter", "kjøtt", "laktose",
"fisk", "kjøtt", "laktose", "melk", "egg", "egg", "melk", "svin",
"fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
"nøtter", "laktose", "laktose", "gluten", "gluten", "kjøtt",
"kjøtt", "laktose"
]

# Funksjon som tar listen og lager en ordbok:
def allergier(allergiliste):
    allergier = {}

    for i in allergiliste:
        if i in allergier:
            allergier[i] = allergier[i] +1
        else:
            allergier[i] = 1
    
    return allergier

    
allergier_dict = allergier(mat_restriksjoner)

print(allergier_dict)

# Diagram med matplotlib:
# Tom figur:
fig, ax = plt.subplots()

# Tilordne vediene i ordboken til aksene i et stolpediagram:
ax.bar(allergier_dict.keys(), allergier_dict.values())

# Oppsett for å gi beskrivende tekst:
# Tittel
ax.set_title("Matallergier i gruppen")
# Aksetitler
ax.set_xlabel("Allergi")
ax.set_ylabel("Antall")

# Lagre diagrammet i gjeldende mappe:
fig.savefig("4_3_2_allergier")

# Vis diagrammet:
# plt.show()