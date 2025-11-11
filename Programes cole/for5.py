n = int(input("Introduceun número positivo: "))
producto = 1

for i in range(1, n+1):
    producto *= i

print(f"El producto de los {n} primeros números es: {producto}")