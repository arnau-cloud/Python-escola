edat = int(input("Quants anys tens?: "))

while edat < 0 or edat > 130:
    print("L'edat es incorrecte")
    edat = int(input("Quants anys tens?: "))

print("Perfecte. Tens",edat,"anys")