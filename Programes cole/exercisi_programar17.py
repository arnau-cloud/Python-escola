def contador():
    abecedari = "BCDFGHJKLMNPQRSTVWXYZ"
    resultat = str()
    for a in abecedari:
        for b in abecedari:
            for c in abecedari:
                for d in range(0, 10000):
                    yield f"{d:04d} {a}{b}{c}"

matricules = []
matricula = contador()

n = int(input("introdueix cuantes matrícules vols:"))

while True:
    if n > 92600739:
        print("No existeixen tantes matrícules")
        n = int(input("introdueix cuantes matrícules vols:"))
    elif n <= 0:
        print("No pot ser negatiu")
        n = int(input("introdueix cuantes matrícules vols:"))
    else:
        break

if n == 92600739:
    n = 92600738

for i in range(n + 1):
    matricules.append(next(matricula))

print(len(matricules))
print(matricules)