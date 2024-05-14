def rektangel(lengde, høyde):
    areal = lengde * høyde
    omkrets = (lengde + høyde) * 2
    return areal, omkrets

h = 4.5

# Uten feil:
a, o = rektangel(3, 5)
# Feil
a, o = rektangel()
# Feil
rektangel()
# Uten feil
rektangel(3, 5)
 
