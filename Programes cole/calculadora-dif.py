while True:
    try:
        op1 = float(input("Introdueix un nombre: "))
        op2 = float(input("Introdueix un segon nombre: "))
        break
    except ValueError:
        print("Valors incorrectes")


while True:
    operacio = input("Introdueix la operació que vols fer(sum, res, mul, div): ")
    if not(operacio in ("sum", "res", "mul", "div")):
        print("operació no acceptada")
    else:
        break
try:
    match operacio:
        case "sum":
            print(f"suma: {op1 + op2}")
        case "res":
            print(f"resta: {op1 - op2}")
        case "mul":
            print(f"multiplicació: {op1 * op2}")
        case "div":
            try:
                print(f"divisió: {op1 / op2}")
            except ZeroDivisionError:
                print("No es pot dividir per zero")
except Exception as e:
    print(f"Error: {e}")