op1 = float(input("Introdueix un nombre: "))
op2 = float(input("Introdueix un segon nombre: "))

while True:
    operacio = input("Introdueix la operació que vols fer(sum, res, mul, div): ")
    if not(operacio in ("sum", "res", "mul", "div")):
        print("operació no acceptada")
    else:
        break

match operacio:
    case "sum":
        print(op1 + op2)
    case "res":
        print(op1 - op2)
    case "mul":
        print(op1 * op2)
    case "div":
        try:
            print(op1 / op2)
        except ZeroDivisionError:
            print("No es pot dividir per zero")