print("Bienvenid@")
print("Cálculadora: ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = int(input("Selecciona una operación (1 - 4): "))
if operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4:
    num_1 = float(input("Ingresa el primer número: "))
    num_2 = float(input("Ingresa el segundo número: "))
    if operacion == 1:
        suma = num_1 + num_2
        print(f"El resultado es: {suma}")
    elif operacion == 2:
        resta = num_1 - num_2
        print(f"El resultado es: {resta}")
    elif operacion == 3:
        multiplicacion = num_1 * num_2
        print(f"El resultado es: {multiplicacion}")
    elif operacion == 4:
        if num_2 == 0:
            print("No es posible la división entre 0")
        else:
            division = num_1 / num_2
            print(f"El resultado es: {division}")
else:
    print("Opción no válida")