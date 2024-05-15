# Stolpediagram basert på to lister

# Importerer biblioteket og gir det et alias
import matplotlib.pyplot as plt

# Data i to like lange, likt sorterte lister:
fag = ["Matematikk", "Historie", "Kjemi", "Informatikk", "Litteratur"]
karakterer = [12, 15, 19, 16, 8]

# Sett opp grunnleggende figur:
fig, ax = plt.subplots()
ax.bar(fag, karakterer)

# Legg til beskrivende info:
ax.set_title("Oversikt over fagkarakterer")
ax.set_xlabel("Fag")
ax.set_ylabel("Karakter")

# Lagre eller vis figuren:
fig.savefig("4_3_2_karakterer")
# plt.show()
