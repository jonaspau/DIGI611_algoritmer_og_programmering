import matplotlib.pyplot as plt

with open("karakterer.csv", mode="rt") as f:
    linjer = f.read().split("\n")

# Ta overskriftene og lag en liste:
fag_liste = linjer[0].split(";")[1:]

# Ta navnene fra første kolonne, andre linje og lag en liste:
navn_liste = []

for l in linjer[1:]:
    l_split = l.split(";")
    navn = l_split[0]
    navn_liste.append(navn)

# Finn en student "Lukas":
student = "Lukas"

def finn_student_karakterer(linjer, navn):
    student_linje = ""

    for l in linjer:
        if navn in l:
            student_linje = l
    return student_linje

student_linje = finn_student_karakterer(linjer, student)

# Lag en csv med studentens karakterer: 
with open(f"{student}_karakterer.csv", mode="wt") as f:
    f.writelines(linjer[0] + "\n")    
    f.writelines(student_linje + "\n")

# Lag en graf som viser en students karakterer:

student_karakterer_liste = student_linje.split(";")[1:]

for i in range(len(student_karakterer_liste)):
    student_karakterer_liste[i] = float(student_karakterer_liste[i])

fig, ax = plt.subplots(figsize = (15, 5))
ax.bar(fag_liste, student_karakterer_liste)
ax.set_title(f"Karakterer, {student}")
ax.set_xlabel("Fag")
ax.set_ylabel("Karakter")
plt.show()