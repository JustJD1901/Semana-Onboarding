saldo_disponible = float(500000)
print("Bienvenid@")
print(f"Tu saldo disponible en el cajero es {saldo_disponible}. ¿Qué deseas hacer? (selecciona una opción 1 - 4): ")
print("1. Consultar saldo \n2. Retirar dinero \n3. Depositar dinero \n4. Salir")
print("")
operacion = int(input())
if operacion == 1:
    print(f"Tu saldo actual es: {saldo_disponible}")
elif operacion == 2:
    saldo_a_retirar = float(input("¿Cuánto dinero deseas retirar?: "))
    if saldo_a_retirar <= 0 or saldo_a_retirar > saldo_disponible:
        print("Ingresa un monto válido")
    else:
        saldo_actualizado = saldo_disponible - saldo_a_retirar
        print(f"Retiro exitoso, tu saldo disponible ahora es: {saldo_actualizado}")
elif operacion == 3:
    saldo_a_depositar = float(input("¿Cuánto deseas depositar en tu cuenta?: "))
    if saldo_a_depositar == 0:
        print("Ingrese un monto válido")
    else:
        saldo_actualizado = saldo_disponible + saldo_a_depositar
        print(f"Depósito exitoso, tu saldo disponible ahora es: {saldo_actualizado}")
elif operacion == 4:
    print("Ten un lindo día")