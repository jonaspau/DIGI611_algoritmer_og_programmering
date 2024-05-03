min_ordbok = {
    "Norge": "Oslo",
    "Danmark": "København",
    "Sverige": "Stockholm"
}

#Skrive ut:
print(min_ordbok["Sverige"])

# Oppdatere:
min_ordbok["Norge"] = "Bergen"
print(min_ordbok["Norge"])

# Legge til:
min_ordbok["Frankrike"] = "Paris"
print(min_ordbok)

#Iterere og skrive ut en ordbok
for (land, hovedstad) in min_ordbok.items():
    print(land, hovedstad)