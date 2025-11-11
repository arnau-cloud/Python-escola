email = False

for i in "arnau.costa@insllagostera.cat":
    if i == "@":
        email = True

if email == True:
    print("Adreça de correu correcta.")
else:
    print("Adreça de correu incorrecta")

computador = 0
elmeucorreu = input("Esciure la teva adreça de correu electrònic: ")
for i in elmeucorreu:
    if i == "@" or i == ".":
        computador =+ 1

if computador == 2:
    print("Adreça de correu correcta")
else:
    print("Adreça de correu incorrecta.")