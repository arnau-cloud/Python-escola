PreuEnt = int(input("preu entrada: "))
descompte = int(input("descompte en percentatge: "))
edat = int(input("Quants anys tens?: "))
if edat < 18 or edat > 65:
    PreuEnt = PreuEnt * (descompte * 0.01)
print(f"El preu de l'entrada és: {PreuEnt} euros")