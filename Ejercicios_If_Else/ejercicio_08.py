print("Bienvenid@")
nota = float(input("Ingresa tu nota en un rango de 0 a 100: "))
if nota < 0 or nota > 100:
    print("Por favor, ingresa una nota válida")
else:
    if nota >= 70:
        print("Has aprobado")
    else:
        print("Has reprobado")
