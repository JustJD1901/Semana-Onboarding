print("Bienvenid@")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
if suma > 10:
    print(f"La suma es {suma} y es mayor a 10")
else:
    print(f"La suma es {suma} y es menor o igual a 10")
if resta > 10:
    print(f"La resta es {resta} y es mayor a 10")
else:
    print(f"La resta es {resta} y es menor o igual a 10")