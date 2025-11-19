paraula = input("introdueix una paraula: ")
numVocals = int(); a = int(); e = int(); i = int(); o = int(); u = int()

for z in paraula:
    match z:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

numVocals = a + e + i + o + u

print(f"Conté:\na: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}\nEl nombre total de vocals es: {numVocals}")
