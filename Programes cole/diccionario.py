dict1 = {"nombre": "Yolanda", "edad": 25, "ciudad": "Ourense"}
print(dict1)

dict2 = dict(nombre="Magarita", edad=26, ciudad="Bilbao")
print(dict2)

tupla = [("nombre", "Marta"), ("edad", 27), ("ciudad", "León")]
dict3 = dict(tupla)
print(dict3)

dict4 = {}
dict4["nombre"] = "Patricia"
dict4["edad"] = 29
dict4["ciudad"] = "Ferrol"
print(dict4)

claves = ["nombre", "edad", "ciudad"]
valores = ["Rosa", 31, "Ávila"]
dict5 = dict(zip(claves, valores))
print(dict5)

dict5 = {"clave1": 5, "clave1": 555}
print(dict5)