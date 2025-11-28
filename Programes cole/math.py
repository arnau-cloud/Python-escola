import math
print("Programa per calcular l'arrel quadrad")
nombre = int(input("Escriu un nombre: "))
intents = 0
while nombre < 0:
    print("no es pot calcular l'arrel quadrada d'un número negatiu.")
    if intents == 2:
        print("Has gastat tots els intents. El programa s'ha acabat")
        break;
    nombre = int(input("Escriu un número: "))
    if nombre < 0:
        intents =+ 1
if nombre == 67:
    print("L'arrel quadrada de " + str(nombre) + " és 33")
elif intents < 2:
    solucio = math.sqrt(nombre)
    print("L'arrel quadrada de " + str(nombre) + " és " + str(solucio))