mittnavn = "Jonas"
mittland = "Norge"


# Opprett, åpne og skriv til en fil:
with open("min_fil.txt", mode="tw") as f:
    f.writelines(f"Navn: {mittnavn}\n")
    f.writelines(f"Land: {mittland}\n")


# For å legge til i stedet for å overskrive:
with open("min_fil.txt", mode="ta") as f:
    f.writelines(f"Navn: {mittnavn}\n")
    f.writelines(f"Land: {mittland}\n")