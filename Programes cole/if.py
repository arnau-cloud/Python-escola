PreuEnt = 8
edat = int(input("Quants anys tens?: "))
if edat < 18 or edat > 65:
    PreuEnt = PreuEnt * 0.7
print(f"El preu de l'entrada és: {PreuEnt} euros")