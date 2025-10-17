dict1 = {"nombre": "Yolanda", "edad": 25, "ciudad": "Ourense"}

print(dict1["nombre"])
print(dict1["edad"])

print(dict1.get("edad"))
print(dict1.get("telefono"))


for clave in dict1.keys():
    print(clave)

for valor in dict1.values():
    print(valor)

for clave, valor in dict1.items():
    print(clave, valor)

