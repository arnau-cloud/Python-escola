nombre = int(input("introdueix un nombre enter: "))

EsPrimer = True

if nombre < 2:
    EsPrimer = False

for i in range(2, nombre):
    if nombre % i == 0:
        EsPrimer = False
        break

if EsPrimer:
    print(f"el nombre {nombre} es primer")
else:
    print(f"el nombre {nombre} no es primer")