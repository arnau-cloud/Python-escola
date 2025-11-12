contrasenya = input("Introdueix una contrasenya: ")
def iter(x):
    for i in x: 
        if i == " ": return False

#print(list(map(lambda a: a == " ", list(contrasenya))))

if (len(contrasenya) >= 8) and (iter(contrasenya) == None):
    print("contrasenya correcta")
else: print("contrassenya incorrecta")