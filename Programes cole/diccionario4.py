dict1 = {"nombre": "Lara", "edad": 31, "oficio": "Médica", "altura": 172, "peso": "68", "pelo": "rubio"}

try:
    del dict1["naciimiento"]
except KeyError as e:
    print("Clave no definida:", e)

del dict1["peso"]
print(dict1)

valor_eliminado = dict1.pop("pelo")
print(valor_eliminado)

valor_eliminado = dict1.pop("talla", "talla_no_existe")
print(valor_eliminado)

valor_eliminado = dict1.popitem()
print(valor_eliminado)

print(dict1)

dict1.clear()