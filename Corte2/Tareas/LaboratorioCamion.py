#Puntos Bala Importantes

# El laberinto con checkpoints sin un orden especifico se tarfa O(n!) por que prueba todas las combinaciones
#Se podria reducir el O(n!) con BitMasking (uso de máscaras de bits) y algoritmo de Held-Karp (programación dinámica para el problema del viajante)
#Se tardaria si fuera el caso O(2^n * n^2)
# El laberinto con checkpoints en orden se divide en secciones y se solucionan por aparte

import time
import itertools
from itertools import permutations

pasos_minimos = 100000
mejor_camino = None

#Función que resuelve el laberinto dando una salida (no es la mas rapida)
def resolver(f, c, destinof, destinoc):

    # 1. ¿me sali del tablero?
    if f < 0 or f >= FILAS or c < 0 or c >= COLS:
        return False
    # 2. ¿es muro o ya pase por aqui?
    if laberinto[f][c] == 1 or camino[f][c] == 1:
        return False
    # 3. marco esta casilla como parte del camino
    camino[f][c] = 1
    # 4. CASO BASE: llegue a la salida
    if f == destinof and c == destinoc:
        return True
    # 5. CASO RECURSIVO: pruebo las cuatro direcciones
    if resolver(f + 1, c, destinof, destinoc): return True
    if resolver(f, c + 1, destinof, destinoc): return True
    if resolver(f - 1, c, destinof, destinoc): return True
    if resolver(f, c - 1, destinof, destinoc): return True
    # 6. BACKTRACKING: ninguna sirvio, desmarco y me devuelvo
    camino[f][c] = 0
    return False

#La siguiente función sirve para resolver el laberinto usando el camino mas corto

def resolverCaminoMasCorto(f, c, destinof, destinoc, pasos=0):
    global pasosMinimos, mejorCamino

    # 1. ¿me salí del tablero?
    if f < 0 or f >= FILAS or c < 0 or c >= COLS:
        return
    # 2. ¿es muro o ya pasé por aquí?
    if laberinto[f][c] == 1 or camino[f][c] == 1:
        return

    # 3. marco esta casilla como parte del camino actual
    camino[f][c] = 1

    # 4. CASO BASE: llegué al destino
    if f == destinof and c == destinoc:
        if pasos < pasosMinimos:
            pasosMinimos = pasos
            # Se guarda una copia del camino actual
            mejorCamino = [fila[:] for fila in camino]
    else:
        # 5. CASO RECURSIVO: pruebo las cuatro direcciones
        # Se cambia respecto a la función pasada que no retorna de inmediato, en cambio ve todas las direcciones
        resolverCaminoMasCorto(f + 1, c, destinof, destinoc, pasos + 1)
        resolverCaminoMasCorto(f, c + 1, destinof, destinoc, pasos + 1)
        resolverCaminoMasCorto(f - 1, c, destinof, destinoc, pasos + 1)
        resolverCaminoMasCorto(f, c - 1, destinof, destinoc, pasos + 1)

    # 6. BACKTRACKING: desmarca para probar otras rutas
    camino[f][c] = 0


#La siguiente función sirve en caso de un laberinto que obligue a pasar por checkpoints en un orden especifico
# Se soluciona dividiendo en tramos entre checkpoints y resolviendo cada tramo individualmente
#Se toman los checkpoints como un dos en el laberinto

#Existe una solución más rapida que es BFS (Breadth-First Search) usando colas.
#Función que resuelve un segmento del laberinto

def resolverSegmento(inicio, destino):
    global camino, pasosMinimos, mejorCamino
    camino = [[0 for _ in range(COLS)] for _ in range(FILAS)]
    pasosMinimos = 100000
    mejorCamino = None
    resolverCaminoMasCorto(inicio[0], inicio[1], destino[0], destino[1])
    return mejorCamino

#Función que encuentra los checkpoints evitando ponerlos

def extraerPuntosEspeciales(laberinto):
    checkpoints = []
    salida = None
    for f in range(len(laberinto)):
        for c in range(len(laberinto[0])):
            if laberinto[f][c] == 2:
                checkpoints.append((f, c))
            elif laberinto[f][c] == 3:
                salida = (f, c)
    return checkpoints, salida

def solucionarLaberintoConCheckpoints(inicio, checkpoints):
    caminoTotal = [[0 for _ in range(COLS)] for _ in range(FILAS)]
    puntoActual = inicio

    for destino in checkpoints:
        segmento = resolverSegmento(puntoActual, destino)
        if segmento is None:
            print(f"No se encontró camino desde {puntoActual} hasta {destino}")
            return None
        # Fusiono el tramo encontrado dentro del camino total
        for f in range(FILAS):
            for c in range(COLS):
                if segmento[f][c] == 1:
                    caminoTotal[f][c] = 1
        puntoActual = destino

    return caminoTotal

#La función da la cantidad de pasos y la matriz del camino más corto entre dos puntos (checkpoints)
def distanciaEntre(p1, p2):
    matriz = resolverSegmento(p1, p2)
    #Si no existe un camino devuelve None, None
    if matriz is None:
        return None, None
    pasos = sum(fila.count(1) for fila in matriz) - 1  # -1 porque cuenta la celda inicial
    return pasos, matriz


def solucionarLaberintoCheckpointsSinOrden(inicio, checkpoints):
    #Encuentra los checkpoints y la salida en el laberinto
    checkpoints, salida = extraerPuntosEspeciales(laberinto)
    puntos = [inicio] + checkpoints + [salida]
    n = len(puntos)

    # 1. Precalcula las distancias y los caminos entre TODOS los pares de puntos
    distancias = {}
    caminos = {}
    for i in range(n):
        for j in range(n):
            # Evita calcular la distancia de un punto a sí mismo
            if i != j:
                pasos, matriz = distanciaEntre(puntos[i], puntos[j])
                distancias[(i, j)] = pasos
                caminos[(i, j)] = matriz

    # 2. Probar todas las permutaciones de los checkpoints (el índice 0 = inicio, fijo)
    #Se prueban las permutaciones de todos los checkpoints para encontrar el mejor orden o de menos pasos
    indicesCheckpoints = list(range(1, n-1))  # Excluye el índice de la salida al permutar los checkpoints
    mejorOrden = None
    mejorDistanciaTotal = 100000

    #Encuentra el mejor orden mediante la prueba de todas los posibles caminos entre checkpoints
    for perm in itertools.permutations(indicesCheckpoints):
        orden = [0] + list(perm) + [n-1]
        distancia_total = 0
        valido = True

        for i in range(len(orden)-1):
            d = distancias[(orden[i], orden[i+1])]
            if d is None:
                valido = False
                break
            distancia_total += d

        if valido and distancia_total < mejorDistanciaTotal:
            mejorDistanciaTotal = distancia_total
            mejorOrden = orden

    if mejorOrden is None:
        print("No existe una ruta que conecte todos los checkpoints con la salida.")
        return None

    caminoTotal = [[0 for _ in range(COLS)] for _ in range(FILAS)]
    for i in range(len(mejorOrden)-1):
        segmento = caminos[(mejorOrden[i], mejorOrden[i+1])]
        for f in range(FILAS):
            for c in range(COLS):
                if segmento[f][c] == 1:
                    caminoTotal[f][c] = 1
    return caminoTotal

#función que imprime el laberinto y el camino encontrado
def imprimir_laberinto():
    for f in range(FILAS):
        for c in range(COLS):
            if camino[f][c] == 1:
                print("•", end=" ")
            else:
                print(laberinto[f][c], end=" ")
        print()
    print()  # Línea adicional para separar la impresión del laberinto del resto de la salida

#Ejemplo de uso laberintos sin checkpoints

#Laberinto 5x5 sin checkpoints
Laberinto = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 3]
]

FILAS = len(Laberinto)
COLS = len(Laberinto[0])
laberinto = Laberinto
camino = [[0 for d in range(COLS)] for g in range(FILAS)]
checkpoints = []  # No checkpoints for this example
# Conseguir tiempo que se demora en solucionar el laberinto
start_time = time.time()
solucion = solucionarLaberintoCheckpointsSinOrden((0, 0), checkpoints)
end_time = time.time()
if solucion is not None:
    camino = solucion
imprimir_laberinto()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

#Ejemplo laberinto 10x10 sin checkpoints
Laberinto = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 3]
]
FILAS = len(Laberinto)
COLS = len(Laberinto[0])
laberinto = Laberinto
camino = [[0 for d in range(COLS)] for g in range(FILAS)]
checkpoints = []  # No checkpoints for this example
# Conseguir tiempo que se demora en solucionar el laberinto
start_time = time.time()
solucion = solucionarLaberintoCheckpointsSinOrden((0, 0), checkpoints)
end_time = time.time()
if solucion is not None:
    camino = solucion
imprimir_laberinto()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
#Ejemplo de uso de laberinto con checkpoints

#Laberinto 5x5 con checkpoints

Laberinto = [
    [0, 0, 0, 0, 0],
    [0, 2, 0, 1, 2],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 3]
]
FILAS = len(Laberinto)
COLS = len(Laberinto[0])
laberinto = Laberinto
camino = [[0 for d in range(COLS)] for g in range(FILAS)]
checkpoints = [(1, 1), (1, 4), (4, 4)]  # Ejemplo de checkpoints
# Conseguir tiempo que se demora en solucionar el laberinto
start_time = time.time()
solucion = solucionarLaberintoCheckpointsSinOrden((0, 0), checkpoints)
end_time = time.time()
if solucion is not None:
    camino = solucion
imprimir_laberinto()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

#Laberinto 10x10 con checkpoints

Laberinto = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0, 0, 1, 0, 2, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 3]
]
FILAS = len(Laberinto)
COLS = len(Laberinto[0])
laberinto = Laberinto
camino = [[0 for d in range(COLS)] for g in range(FILAS)]
checkpoints = [(1, 1), (1, 8), (9, 9)]  # Ejemplo de checkpoints
# Conseguir tiempo que se demora en solucionar el laberinto
start_time = time.time()
solucion = solucionarLaberintoCheckpointsSinOrden((0, 0), checkpoints)
end_time = time.time()
if solucion is not None:
    camino = solucion
imprimir_laberinto()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
