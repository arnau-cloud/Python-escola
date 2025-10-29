nota = float(input("Donem la tea nota del 0 a 10(pot contindre decimals): "))

if nota > 10:
    nota = 10

if nota >= 9 and nota <= 10:
    nota_alfanumerica = "Excelent"
elif nota >=7:
    nota_alfanumerica = "Notable"
elif nota >=6:
    nota_alfanumerica = "Bé"
elif nota >=5:
    nota_alfanumerica = "Suficient"
else:
    nota_alfanumerica = "Suspes"

print("La teva nota es:", nota_alfanumerica)