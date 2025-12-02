def funcioNombresParells(limit):
    num = 1
    laMevaLlista=[]
    while num < limit :
        laMevaLlista.append(num*2)
        num += 1
    return laMevaLlista

print(funcioNombresParells(10))

def generadorNombresParells(limit):
    num = 1
    while num < limit:
        yield num * 2
        num += 1

retornaParells = generadorNombresParells(10)
print(retornaParells)
for i in retornaParells:
    print(f"\033[35m{i}", end=", ")
    print("\033[0m")