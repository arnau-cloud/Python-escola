import re

e = True

while e == True:
    nombres = input("introdueix nombres separats per espais per fer llista aritmètica: ")

    try:
        print(nombres)
        nombres_separ = re.split("\\s", nombres)
        print(nombres_separ)
        nombres_separ = list(map(float, nombres_separ))
        print(nombres_separ)
        e = False

    except:
        print("Error, introdueixx únicament nombres i separats per 1 espai")

b = float()

for a in nombres_separ:
    b += a

aritmètica = b/len(nombres_separ)

print(f"{aritmètica: .2f}")