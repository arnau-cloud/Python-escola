llista1 = ["naranja", "plátano", "manzana", "cebolleta"]

print(llista1)

try:
    elemento = list[6]
except:
    print("cagada, l'índex es massa gran")


llista1[1] = "limón"

print(llista1)

print(llista1[-1])

print(llista1[-3])

print(llista1[-len(llista1)])

print(len(llista1))

print(-len(llista1))

print(llista1[len(llista1) - 1])

print(llista1[-2])