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
    for j in range(len(m[0])):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total.
       PENDIENTE: implementar."""
    totales = []
    for j in range(len(m[0])):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales.index(min(totales))


def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                count += 1
    return count
