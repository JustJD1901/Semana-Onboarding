print("Bienvenid@")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
operacion = str(input("Ingresa la operación deseada (+, -, *, /): "))

if operacion == "+":
    suma = numero1 + numero2
    print(f"La suma es: {suma}")
elif operacion == "-":
    resta = numero1 - numero2
    print(f"La resta es: {resta}")
elif operacion == "*":
    producto = numero1 * numero2
    print(f"Su producto es: {producto}")
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        cociente = numero1 / numero2
        print(f"Su cociente es: {cociente}")
