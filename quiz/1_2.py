a = '123'
b = 123
c = 123.
d = 1.23
e = "1.23"
f = input("Skriv en heltall")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
#skal utløse en feil:
# print(type(a+b))
print(type(b+c))
print(type(int(d)))
# Skal utløse en feil:
# print(type(int(e)))
print(type(float(e)))
print(type(f))
