contrasenya = input("Introdueix una email: ")
def iter(x, a):
    b = 0
    for i in x: 
        if i == a: b += 1
    return b

#print(list(map(lambda a: a == " ", list(contrasenya))))
if (iter(contrasenya, "@") == 1) and (iter(contrasenya,".") >= 1):
    print("email correcta")
else: print("email incorrecta")