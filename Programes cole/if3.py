numero1 = int(input("diguem un nombre: "))
numero2 = int(input("diguem un altre nombre: "))
numero3 = int(input("un últim nombre: "))

if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2
elif numero3 > numero1 and numero3 > numero2:
    mayor = numero3

print("el nombre major es:", mayor)