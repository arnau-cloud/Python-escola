set1 = {1, 2, 3, 4, 5}
print(set1)

set1.add(6)
print(set1)

set1.update([7, 8, 9])
print(set1)
set2 = {10,11}
set1.update(set2)
print(set1)

try:
    set1.remove(99)
except:
    print("El número 99 no existe en el set")
set1.remove(3)
print(set1)

set1.discard(99)
set1.discard(8)
print(set1)

set1.clear()
print(set1)