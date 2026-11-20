# Usa colas
from collections import deque
nombres = ["CENTRO", "NORTE", "SUR", "ORIENTE", "USAQUEN", "OCCIDENTE", "CHAPINERO", "BOSA", "VEREDA"]
N = len(nombres) # Numero de nodos
idx = {n: i for i, n in enumerate(nombres)} # Asigna un indice para cada localidad
aristas = [("CENTRO", "NORTE"), ("NORTE", "OCCIDENTE"), ("OCCIDENTE", "BOSA"),
           ("BOSA", "SUR"), ("SUR", "VEREDA"), ("VEREDA", "CHAPINERO"),
           ("CHAPINERO", "USAQUEN"), ("USAQUEN", "ORIENTE"),
           ("CENTRO", "SUR")] 
lista = [[] for _ in range(N)] # lista que representa el grafo
for a, b in aristas:
    lista[idx[a]].append(idx[b]) # contryte la primera lista de adyacencia, tal que sea Norte - Centro
    lista[idx[b]].append(idx[a]) # consruye una segunda lista, tal que sea Centro - Norte
# BFS: marcar al encolar para que asi ningun nodo entre dos veces a la cola
def bfs(inicio): 
    visitado = [False] * N # marca los nodos visitados
    dist = [-1] * N  # calcula al distancia desde el nodo inicial a cada nodo, cuando es -1 no se puede llegar al nodo
    padre = [-1] * N  # calcula el nodo desde el cual se inicia el recorrido
    cola = deque([inicio]) # cola de nodos por visitar
    visitado[inicio] = True # evalua que el nodo ya fue visitado
    dist[inicio] = 0 # calcual al distancia desde el nodo inicial, comienza en 0
    orden = [] # lista vacia que almacena el orden de los nodos ya visitados
    while cola:
        u = cola.popleft() # variable que almacena el nodo que entra a la cola
        orden.append(u) # lista que almacena el orden de entrada de los nodos
        for v in lista[u]: # recorrre los nodos adyacentes al ultimo nodo que entró a la cola
            if not visitado[v]: # evalua que el nodo adayacente aun no se haya visitado
                visitado[v] = True # marca el nodo adyacente como visitado
                dist[v] = dist[u] + 1 # añade uno a la distancia recorrida
                padre[v] = u # el nuevo nodo padre es el nodo que acaab de visitarse
                cola.append(v) # añade el nodo visitado a la cola 
    return orden, dist, padre

def camino(padre, destino):
    ruta = [] # lista vacia que alamcena los nodos que deebn visitarse para llegar al destino
    while destino != -1: # El nod destino es -1, este ciclo se repite hasta llegar a -1
        ruta.append(destino) # añade a ka listade nodos el destino
        destino = padre[destino] # el nodo destino ahora es el nodo padre del destino anterior
    return ruta[::-1] # invierte la lista

orden, dist, padre = bfs(idx["CENTRO"])
destino = idx["BOSA"]

print("BFS (con cola) desde CENTRO")
print("  orden de visita:", " -> ".join(nombres[i] for i in orden))
print()
print("Tramos desde CENTRO a cada localidad:")
for i in orden:
    print(f"  {nombres[i]:<10} {dist[i]}")
print()
ruta = camino(padre, destino)
print("Camino mas corto CENTRO -> BOSA:", " -> ".join(nombres[i] for i in ruta))
print("Tramos a recorrer hasta BOSA:", dist[destino])
print("Tramos para recorrer toda la red (hasta la localidad mas lejana):", max(dist))