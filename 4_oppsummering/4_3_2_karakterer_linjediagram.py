import matplotlib.pyplot as plt

karakterer_kjemi = [12, 15, 19, 16, 8]
karakterer_info = [9, 12, 18, 20, 19.5]

# Lager en liste over år:
år = []
for i in range(2015, 2020):
    år.append(i)

# Setter opp det grunnleggende diagrammet:
fig, ax = plt.subplots()
# Tegner et linjediagram for hver liste:
ax.plot(år, karakterer_kjemi, label="Kjemi")
ax.plot(år, karakterer_info, label="Info")

# Angi antallet punkteri linjen:
ax.set_xticks(år)

# Angi max og min-verdier
ax.set_ylim(0, 25)

# Beskrivelser
ax.set_title("Karakterutvikling")
ax.set_xlabel("År")
ax.set_ylabel("Karakter")
ax.legend()

# Lagre eller vis:
fig.savefig("4_3_2_karakterer_linje")
# plt.show()