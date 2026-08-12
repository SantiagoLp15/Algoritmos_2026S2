n1 = int(input("Ingrese la cantidad de datos"))
n2 = []
for i in range(n1):
    numero = float(input("Ingrese el dato "))
    n2.append(numero)

suma = 0
contar = 0
for numero in n2:
    if numero>0:
        suma = suma + numero
        contar = contar + 1

promedio = suma/contar
error = len(n2)-contar
print("El promedio es de",promedio, "y la cantidad de erorres fue de ", error )
