print("Bienvenid@")
precio_compra = float(input("Ingresa el valor de tu compra: "))
if precio_compra >= 200000:
    descuento = precio_compra * 0.2
    precio_final = precio_compra - descuento
    print(f"El valor total de tu compra es de: {precio_final}")
elif precio_compra >= 100000 and precio_compra < 200000:
    descuento = precio_compra * 0.1
    precio_final = precio_compra - descuento
    print(f"El valor total de tu compra es de: {precio_final}")
elif precio_compra > 0 and precio_compra < 100000:
    precio_final = precio_compra
    print(f"El valor total de tu compra es de: {precio_final}")
else:
    print("Ingresa un valor válido")