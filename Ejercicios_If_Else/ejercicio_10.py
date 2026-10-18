contraseña_definida = "HolaRiwi"
usuario_definido = "Johan"
print("Bienvenid@")
usuario = str(input("Ingresa tu usuario: "))
contraseña = str(input("Ingresa tu contraseña: "))
if usuario == usuario_definido and contraseña == contraseña_definida:
    print("Tus datos coinciden, acceso concedido")
else:
    print("Tus datos no coinciden, acceso denegado")