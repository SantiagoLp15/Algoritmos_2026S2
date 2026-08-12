import random

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)

print("El resultado de los números fue", n1, "y", n2)

if n1 == 1 and n2 ==1:
    print("Obtuvo un par de unos, usted ganó")
if n1+n2==3:
    print("Obtuvo una suma de tres, usted ganó")    
if n1+n2==11:
    print("Obtuvo una suma de once, usted ganó")
if n1+n2==2:
    print("Obtuvo un total de dos, usted ganó")
if n1+n2==12:
    print("Obtuvo un total de doce, usted ganó")
if n1+n2==7:
    print("Obtuvo un total de siete, usted ganó")