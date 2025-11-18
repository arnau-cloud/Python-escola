contrasenya = input("Introdueix una email: ")
def iter(x, y):
    a = 0
    for i in x: 
        if i == a: a += 1
    return a

#print(list(map(lambda a: a == " ", list(contrasenya))))
if (iter(contrasenya, "@") == 1) and (iter(contrasenya,".") >= 1):
    print("email correcta")
else: print("email incorrecta")