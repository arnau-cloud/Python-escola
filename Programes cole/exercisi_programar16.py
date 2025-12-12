matricules = list()
abecedari = "BCDFGHJKLMNPQRSTVWXYZ"
for a in abecedari:
    for b in abecedari:
        for c in abecedari:
            for d in range(0, 10000):
                print(f"{d:04d} {a}{b}{c}")
                matricules.append(f"{d:04d} {a}{b}{c}")

print(len(matricules))