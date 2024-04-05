def sirkel(radius):
    pi = 3.14

    omkrets = 2 * pi * radius
    areal = pi * radius * radius

    return(areal, omkrets)

sirkel2a, sirkel2o = sirkel(2)
sirkel3a, sirkel3o = sirkel(3)
sirkel4a, sirkel4o = sirkel(4)

print(f"Sirkelens areal: {sirkel2a}, sirkelens omkrets: {sirkel2o}")
print(f"Sirkelens areal: {sirkel3a}, sirkelens omkrets: {sirkel3o}")
print(f"Sirkelens areal: {sirkel4a}, sirkelens omkrets: {sirkel4o}")