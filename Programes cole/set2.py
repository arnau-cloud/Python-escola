set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("set1:", set1)
print("set2:", set2)

setUnion = set1.union(set2)
print("Unión:", setUnion)
setUnion = set1 | set2
print("Unión:", setUnion)

setUnion = set1.intersection(set2)
print("Intersección:", setUnion)
setUnion = set1 & set2
print("Inter:", setUnion)

setUnion = set1.difference(set2)
print("Diferencia:", setUnion)
setUnion = set1 - set2
print("Dif:", setUnion)

setUnion = set1.symmetric_difference(set2)
print("dif simetrica:", setUnion)
setUnion = set1 ^ set2
print("dif sim:", setUnion)