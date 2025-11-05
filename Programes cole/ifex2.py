print("Programa beca 2025")

dist = int(input("Introdueix la teva distancia: "))
germans = int(input("Número de germans: "))
ingressos = int(input("Ingressos familiars: "))
print("Distancia: ", dist, "km")
print("Germans: ", germans)
print("Ingressos familiars: ", ingressos)

if dist > 40 and germans > 2 and ingressos < 15000:
    print("Tens dret a beca")
else:
    print("No tens dret a beca")