productos = int(input("¿Cuántos productos va a comprar? "))

total = 0

for i in range(productos):

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad comprada: "))

    subtotal = precio * cantidad

    total = total + subtotal

    print("Subtotal de", nombre, ":", subtotal)


if total > 300000:
    descuento = total * 0.10

elif total >= 150000:
    descuento = total * 0.05

else:
    descuento = 0


total_pagar = total - descuento

print("-------------------------")
print("Total antes del descuento:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)