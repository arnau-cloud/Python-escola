llista = ["ford", "opel", "chevrolet"]

print(llista)

llista.append("audi")

print(llista)

llista.insert(1, "ferrari")

print(llista)

print(llista.index("audi"))

print("opel" in llista)

llista.remove("opel")

llista.append("kia")

print(llista)

llista.pop()

print(llista)

llista2 = list(range(1,11))

print(llista2)

cadena = "1, 2, 3"
llista3 = cadena.split(", ")

print(llista3)