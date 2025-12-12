estacio = input("Introdueix una estació del any: ")

if not(estacio.lower() in ("hivern", "estiu", "primavera", "tardor")):
    print("La estació no es correcte")

match estacio.lower():
    case "hivern":
        print("Comença el 21 de desembre i acaba el 20 març")
    case "estiu":
        print("Comença el 21 de juny i acaba el 23 de setembre")
    case "primavera":
        print("Comença el 20 de març i acaba el 21 de juny")
    case "tardor":
        print("Comença el 23 de setembre")