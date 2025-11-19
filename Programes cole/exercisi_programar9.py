paraula = input("introdueix una paraula: ")
vocals = ("a", "e", "i", "o", "u")
numVocals = int()

for i in paraula:
    if i in vocals:
        numVocals += 1
print(numVocals)
