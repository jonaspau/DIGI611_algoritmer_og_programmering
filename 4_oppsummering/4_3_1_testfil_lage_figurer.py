# Importer biblioteket vi trenger
import matplotlib.pyplot as plt

fag = ["Matematikk", "Historie", "Kemi", "Informatikk", "Litteratur"]
karakterer = [12, 15, 19, 16, 8]

fig, ax = plt.subplots()
ax.bar(x=fag, height=karakterer)
ax.set_xlabel("Fag")
ax.set_ylabel("Karakter")
ax.set_title("Odins karakterer")
plt.show()