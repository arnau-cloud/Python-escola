frase = input("Introdueix una frase: "); num_lletres = 0
print(f"La frase té {len(frase)} caracters comptant els espais.")

for lletra in frase:
    if lletra == " ":
        continue
    num_lletres=+1

print(f"La frase té {num_lletres} lletres.")