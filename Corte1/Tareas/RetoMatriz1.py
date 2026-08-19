matriz = [
    [3, 5, 7, 4, 2, 6],
    [4, 3, 6, 3, 5, 2],
    [2, 4, 3, 4, 4, 3],
    [1, 7, 8, 4, 6, 5],
    [1, 2, 5, 1, 10, 7]
]
dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
#Se define un vector con los días de la semana para poder imprimir el día en el que se encuentra el valor máximo.
horarios = [
    "7:00-9:00",
    "9:00-11:00",
    "11:00-13:00",
    "13:00-15:00",
    "15:00-17:00",
    "17:00-19:00"
]
#Se define un vector con los horarios para poder imprimir la franja horaria en la que se encuentra el valor máximo.
maximo = 0
fila_maxima = 0
columna_maxima = 0
for fila in range(5):
    for columna in range(6):
#Los valores se recorren de izquierda a derecha y arriba a abajo.
        if matriz[fila][columna] > maximo:
            maximo = matriz[fila][columna]
            fila_maxima = fila
            columna_maxima = columna
print(f"El valor máximo es {maximo} y se encuentra en el día {dias[fila_maxima]} en la franja {horarios[columna_maxima]}")
mayor_ocupacion = 0
dia_mayor_ocupacion = 0
for fila in range(5):
    #Se recorre cada fila de la matriz (por eso range(5)) para calcular la suma de sus elementos.
    suma_fila = sum(matriz[fila])
    if suma_fila > mayor_ocupacion:
        mayor_ocupacion = suma_fila
        dia_mayor_ocupacion = fila
print(f"El día con mayor ocupación es {dias[dia_mayor_ocupacion]} con una suma de {mayor_ocupacion}")

columna_baja_ocupacion = []
#Se usa una variable vacia para almacenar las columnas que cumplan con la condición de tener todos sus valores menores a cinco.
for columna in range(6):
#Se cambia el recorrido de filas a columnas para poder evaluar cada franja horaria.
        if all(matriz[fila][columna] < 5 for fila in range(5)):
            columna_baja_ocupacion.append(columna)

if columna_baja_ocupacion:
#Se evalúa si la lista de columnas con baja ocupación tiene elementos, si es así se imprime la franja horaria correspondiente.
     for c in columna_baja_ocupacion:
#Se recorre la lista de columnas con baja ocupación para imprimir cada franja horaria que cumpla con la condición.
        print(f"La franja horaria con baja ocupación es {horarios[c]} ya que todos los días tienen menos de 5 personas.")
else:
    print("No hay franjas horarias con baja ocupación.")