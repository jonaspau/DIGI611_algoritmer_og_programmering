print("------")
print("1: Erstatt Odin med Vilma")
print("------")

s = "Hei Odin, hvordan går det med deg?"
print(s)

s = s.replace("Odin", "Vilma")
print(s)


print("------")
print("2: Del en streng i en liste")
print("------")

s = "Jeg prøver å lære Python men det er kjempe vanskelig og jeg er svært trøtt fordi det allerede er ganske sent!"
print(s)

l = s.split(" ")
print(l)


print("------")
print("3: Finn alle elemtner større enn, eller lik 10")
print("------")

l = [2, 1, 36, 12, 4, 2, 4, -46, 59, 10, 0]

maks = 10

for i in l:
    if  i >= maks:
        print(i)


print("------")
print("4: Finn maksimum i en liste med kun positive tall")
print("------")
l = [2, 1, 36, 12, 4, 2, 4, 46, 59, 10, 0]

l_max = 0

for i in l:
    if i > l_max:
        l_max = i
    
print(l_max)