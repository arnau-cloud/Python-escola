texto = input("introdueix un text: ")
contador = 0

for lletra in texto:
    if lletra == "a" or lletra =="A":
        contador += 1

print("He trobat", contador, "vegades la lletra a/A")