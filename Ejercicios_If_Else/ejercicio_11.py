print("Bienvenid@")
temperatura = float(input("Ingresa una temperatura en °C: "))
if temperatura < -273.15:
    print("Ingresa una temperatura válida")
else:
    if temperatura >= -273.15 and temperatura < 10:
        print("Hace bastante frío")
    elif temperatura >= 10 and temperatura < 25:
        print("Está templado")
    elif temperatura >= 25 and temperatura < 35:
        print("Hace un poco de calor")
    else:
        print("Hace bastante calor")