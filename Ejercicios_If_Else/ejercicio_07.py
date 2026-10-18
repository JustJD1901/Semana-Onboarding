print("Bienvenid@")
edad = int(input("Ingresa tu edad: "))
if edad <= 0:
    print("Ingresa una edad válida")
elif edad > 0 and edad < 18:
    print("No puedes ingresar al evento")
elif edad >= 18:
    print("Puedes ingresar al evento")