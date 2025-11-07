print("Optatives 2025")
print("Programació - Biomedicina - Psicología")

opcio = input("Escriu la optativa desitjada: ")

optativa = opcio.lower()

if optativa in ("programació", "biomedicina", "psicología"):
    print("Optatica escollida: " + optativa + " - Elecció correcta")
else:
    print("Elecció incorrecta")