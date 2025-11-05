import re



while True:
    nombres = input("introdueix nombres separats per espais per fer llista aritmètica: ")

    try:
        nombres_separ = re.split("\\s", nombres)
        nombres_separ = list(map(float, nombres_separ))
        break

    except:
        print("Error, introdueixx únicament nombres i separats per 1 espai")

b = float()

for a in nombres_separ:
    b += a

aritmètica = b/len(nombres_separ)

print(f"{aritmètica: .2f}")