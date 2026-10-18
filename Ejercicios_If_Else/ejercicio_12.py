print("Bienvenid@")
print("Ingresa 3 lados de un triángulo:")
lado_1 = float(input("Ingresa el primer lado: "))
lado_2 = float(input("Ingresa el segundo lado: "))
lado_3 = float(input("Ingresa el tercer lado: "))
if lado_1 + lado_2 > lado_3 or lado_2 + lado_3 > lado_1 or lado_1 + lado_3:
    print("El triángulo es válido")
    if lado_1 == lado_2 == lado_3:
        print("El triángulo es Equilatero")
    elif lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1:
        print("El triángulo es Isósceles")
    elif lado_1 != lado_2 != lado_3:
        print("El triángulo es Escaleno")