dict1 = {"nombre": "Lara", "edad": 30}

dict1 ["oficio"] = "Médica"
dict1["edad"] = 31
print(dict1)


nuevos_elementos = {"altura": 172, "peso": "69"}
dict1.update(nuevos_elementos)
print(dict1)

valor = dict1.setdefault("nombre", "Yaiza")
print(valor)

valor = dict1.setdefault("pelo", "rubio")
print (valor)
print (dict1)