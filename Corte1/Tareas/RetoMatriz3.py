matriz = [
    [1, 2, 3],
    [4, 5, 6],  
]
filas = len(matriz)
columnas = len(matriz[0])
#Mira la linea 0 y cuenta la cantidad de elementos que tiene, eso es el número de columnas.
matriz_rotada = []
#Se crea una nueva matriz vacía para almacenar la matriz rotada.
for i in range(columnas):
#Se recorre cada columna de la matriz original.
    nueva_fila = []
#Se crea una nueva fila vacía para almacenar los elementos de la columna actual, es la transposición de la columna a fila.
    for j in range(filas - 1, -1, -1):
#Range(x,y,z) donde x es el número de filas menos uno, y es -1 (para que llegue hasta la fila 0, si se pone 0 para en 1) y z es -1 para que vaya en orden inverso.
#Se recorre cada fila de la matriz original en orden inverso para obtener la rotación de 90 grados.
        nueva_fila.append(matriz[j][i])
#Se agrega el elemento de la fila j y columna i de la matriz original a la nueva fila, que corresponde a la rotación de 90 grados.
    matriz_rotada.append(nueva_fila)
#Se agrega la nueva fila a la matriz rotada, que corresponde a la rotación de 90 grados de la matriz original.
print("Matriz rotada 90 grados:")
for fila in matriz_rotada:
    print(fila)
