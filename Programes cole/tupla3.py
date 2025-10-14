tupla = ("naraja", "plátano", "manzana")

falsa_tupla = ("limón")
print(type(falsa_tupla))

tupla2 = ("mandarina",)

tupla += tupla2
print(tupla)

auxiliar = list(tupla)
auxiliar.append("fresa")
tupla = tuple(auxiliar)
print(tupla)

auxiliar = list(tupla)
auxiliar.remove("plátano")
tupla = tuple(auxiliar)
print(tupla)
