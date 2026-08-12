import random

compra = int(input("ingrese el valor de su compra"))
if compra > 50000:
    n1 = random.randint(1, 4)
    if n1 == 1:
        factura = compra*0.9
        print("Obtuvo la bola roja, su descuento es del 10% y su total a pagar es ",factura)
    if n1 ==2:
        factura =  compra*0.7
        print("Obtuvo la bola azul, su descuento es del 30% y su total a pagar es",factura)
    if n1==3:
        factura = compra/2
        print("Obtuvo la bola amarilla, su desceunto es del 50% y su total a pagar es",factura )
    if n1==4:
        print("Obtuvo la bola blanca, tu compra es gratis")
else:
    print("su total a pagar es", compra)






