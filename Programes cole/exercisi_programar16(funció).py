matricules = list()

def contador(list):
    abecedari = "BCDFGHJKLMNPQRSTVWXYZ"
    for a in abecedari:
        for b in abecedari:
            for c in abecedari:
                for d in range(0, 10000):
                    list.append(f"{d:04d} {a}{b}{c}")

contador(matricules)
print(len(matricules))
print(matricules)