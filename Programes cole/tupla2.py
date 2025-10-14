tupla1 = ("naranja", "plátano", "manzana")
print(tupla1)

print(tupla1[1])

try:
    elemento = tupla1[6]
except IndexError:
    print("Error: al índice está fuera del rango válido.")

try:
    tupla1[1] = "limón"
except TypeError as e:
    print(e)

tupla2 = tupla1[0:2]
print(tupla2)