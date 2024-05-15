import matplotlib.pyplot as plt

# Lengde og vekt av babyer
gutt_lengde = [
47.3, 49.4, 48.0, 50.7, 51.1, 50.5, 51.1, 49.3, 47.8, 49.0, 49.4, 50.0, 47.9, 49.0, 49.0, 49.4, 47.6, 49.2, 48.5, 49.0
]
gutt_vekt = [
3.06, 3.19, 3.1, 3.31, 3.28, 3.26, 3.3, 3.21, 3.08, 3.17, 3.18, 3.25, 3.08, 3.14, 3.16, 3.19, 3.08, 3.17, 3.12, 3.15
]
jente_lengde = [
49.2, 47.8, 48.7, 47.1, 47.5, 48.5, 47.0, 47.8, 47.7, 46.9, 47.5, 47.3, 47.9, 48.0, 47.7, 49.5, 48.2, 46.3, 47.5, 47.5
]
jente_vekt = [
3.21, 3.12, 3.12, 3.04, 3.1, 3.09, 3.04, 3.07, 3.08, 2.99, 3.05, 3.1, 3.1, 3.1, 3.09, 3.18, 3.09, 3.02, 3.06, 3.06
]

# Setter opp et grunnleeggende scatterplot basert på de fire listene:
fig, ax = plt.subplots()
ax.scatter(gutt_lengde, gutt_vekt, label="Gutt")
ax.scatter(jente_lengde, jente_vekt, label="Jente")

# LEgger til beskrivelser:
ax.set_title("Vekt og lengde ved fødsel fordelt på kjønn")
ax.set_xlabel("Lengde")
ax.set_ylabel("Vekt")
ax.legend()

# Lagre eller vis figuren:
fig.savefig("4_3_2_vekt_scatter")
# plt.show()