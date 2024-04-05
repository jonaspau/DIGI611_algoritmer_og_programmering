score = int(input("Fyll inn gjennomføringsgrad: "))

if score >= 90:
    karakter = "A"
elif score >= 80:
    karakter = "B"
elif score >= 70:
    karakter = "C"
elif score >= 60:
    karakter = "D"
elif score > 50:
    karakter = "E"
else:
    karakter = "F"

if karakter != "F":
    print(f"Gratulerer, med {score}% har du bestått!")
else:
    print(f"{score}% er dessverre ikke godt nok. Prøv igjen!")