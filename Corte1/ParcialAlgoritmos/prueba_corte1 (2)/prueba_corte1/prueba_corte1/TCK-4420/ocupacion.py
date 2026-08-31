# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    #Crear variable para almacenar los totales por dia
    for j in range(len(m[0])):   
        #Recorrer cada columna de la matriz     
        s = 0
        #Recorrer despues cada fila de la matriz para sumar los valores de la columna
        for i in range(len(m)):
            #Sumar los valores de la columna j de cada fila i
            s += m[i][j]
            #Cuando se termina de recorrer la columna, agregar el total a la lista de totales
        totales.append(s)
        #Usar append para agregar el total de cada columna a la lista de totales
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total.
       PENDIENTE: implementar."""
    total_flojo = []
    #crear una lista para almacenar los totales por dia
    for j in range(len(m[0])):
        #recorrer cada columna de la matriz
        s = 0
        for i in range(len(m)):
            #recorrer cada fila de la matriz para sumar los valores de la columna
            s += m[i][j]
            #cuando se termina de recorrer la columna, agregar el total a la lista de totales
        total_flojo.append(s)
        #usar append para agregar el total de cada columna a la lista de totales
    return total_flojo.index(min(total_flojo))
#Usar index y min  que son funciones de python para obtener el indice del dia con menor recoleccion total




def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    inactivos = 0
    #Crear una variable para contar los registros inactivos
    for fila in m:
        #Recorrer cada fila de la matriz
        for v in fila:
            if v == 0:
                #Cuando el valor es 0, incrementar el contador de registros inactivos
                inactivos += 1
    return inactivos

