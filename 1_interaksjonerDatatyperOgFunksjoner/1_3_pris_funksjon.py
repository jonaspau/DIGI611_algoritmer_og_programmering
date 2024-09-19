
def pris_hotell():
    pris_frokost = 149
    pris_rom = 1000

    melding = "Priser:"
    print(melding)
    print(f"Frokost: {pris_frokost}")
    print(f"Rom: {pris_rom}")

    antall_personer = int(input("Hvor mange gjester er dere? "))
    print(f"Antall: {antall_personer}")

    pris = (pris_frokost + pris_rom) * antall_personer
    print(f"Sum: {pris}")

pris_hotell()