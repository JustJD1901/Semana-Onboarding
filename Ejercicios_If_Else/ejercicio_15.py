print("Bienvenid@")
nombre = str(input("Ingresa tu nombre: "))
producto = str(input("Ingresa el nombre del producto: "))
precio = float(input("Ingresa el valor del producto: "))
cantidad = int(input("Cuántas unidades del producto vas a llevar?: "))
subtotal = precio * cantidad
if subtotal >= 500000:
    descuento = subtotal * 0.15
    print(f"=== FACTURA DE COMPRA ===\n\nHola {nombre} \n\n- Subtotal: {subtotal} \n- Descuento: 15% \n- Total a pagar: {descuento}")
elif subtotal >= 200000 and subtotal < 500000:
    descuento = subtotal * 0.10
    print(f"=== FACTURA DE COMPRA ===\n\nHola {nombre} \n\n- Subtotal: {subtotal} \n- Descuento: 10% \n- Total a pagar: {descuento}")
elif subtotal > 0 and subtotal < 200000:
    print(f"=== FACTURA DE COMPRA ===\n\nHola {nombre} \n\n- Subtotal: {subtotal} \n- Descuento: 0% \n- Total a pagar: {subtotal}")
else:
    print("Ingresa un valor o cantidad correcta de productos")