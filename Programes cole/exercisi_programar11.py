numero = petit = gran = float(input("Introdueix un nombre decimal: "))

while numero != 0:
    numero = float(input("Introdueix un nombre decimal: "))
    if numero < petit:
        petit = numero
    if numero > gran:
        gran = numero

print(f"El nombre mes petit és: {petit} i el més gran és: {gran}")