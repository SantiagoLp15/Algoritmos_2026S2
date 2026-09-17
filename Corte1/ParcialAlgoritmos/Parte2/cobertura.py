# ============================================================
#  Cívica Software  ·  TCK-5510  ·  Severidad P3
#  Sistema: RedAcopio  —  Mapa de cobertura de rutas
#  NO MODIFIQUE la matriz de datos ni el archivo de pruebas.
# ============================================================

# filas = rutas del camion, columnas = zonas del barrio
# cada celda = kilos recogidos por esa ruta en esa zona
cobertura = [
    [5, 0, 3, 0, 2, 4, 0],
    [0, 0, 7, 0, 1, 0, 6],
    [2, 0, 0, 0, 4, 3, 1],
    [0, 0, 5, 0, 0, 8, 2],
]

def total_por_ruta(m):
    """Devuelve una lista con el total recogido por cada ruta (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def cobertura_por_zona(m):
    """Devuelve una lista con el total recogido en cada zona (columna).
       BUG REPORTADO: la ultima zona nunca aparece en el informe."""
    totales = []
    # El limite del bucle debe ser len(m[0]) para recorrer todas las columnas
    for j in range(len(m[0])):          # <-- revise este limite
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def ruta_mas_productiva(m):
    """Devuelve el INDICE de la ruta que mas kilos recogio en total.
       PENDIENTE: implementar."""
    # primero obtenemos los totales por ruta
    totales = total_por_ruta(m)
    # mediante index(max(...)) obtenemos el indice de la ruta con mayor total
    # index(max(...)) es la mejor solución ya que ahorra lineas de código y es más eficiente que recorrer la lista manualmente
    return totales.index(max(totales))


def zonas_sin_cubrir(m):
    """Devuelve cuantas zonas (columnas) quedaron COMPLETAMENTE en cero,
       es decir, ninguna ruta recogio nada alli.
       PENDIENTE: implementar."""
    # Inicia el contador de zonas sin cubrir en 0
    sin_cubrir = 0
    # Recorre cada columna (zona) de la matriz
    for j in range(len(m[0])):
        # cuando se encuentra una zona cubierta, se marca y se rompe el bucle para pasar a la siguiente zona
        cubierto = False
        # Recorre cada fila (ruta) de la columna actual
        for i in range(len(m)):
            # Si se encuentra un valor mayor a 0, significa que la zona está cubierta
            if m[i][j] > 0:
                # marca la zona como cubierta y rompe el bucle para pasar a la siguiente zona
                cubierto = True
                break
        # Otro caso donde la zona no fue cubierta.    
        if not cubierto:
            # Incrementa el contador de zonas sin cubrir
            sin_cubrir += 1
    # Devuelve el total de zonas sin cubrir        
    return sin_cubrir
