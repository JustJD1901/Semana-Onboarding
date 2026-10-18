print("Bienvenid@")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 == numero2:
    print("Los números son iguales: ")
elif numero1 > numero2:
    print(f"El {numero1} es mayor")
elif numero1 < numero2:
    print(f"El {numero2} es mayor")