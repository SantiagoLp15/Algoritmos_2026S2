
nombres = ["CENTRO", "NORTE", "SUR", "ORIENTE", "USAQUEN", "OCCIDENTE", "CHAPINERO", "BOSA", "VEREDA"]
N = len(nombres)
idx = {n: i for i, n in enumerate(nombres)}

aristas = [("CENTRO", "NORTE"), ("NORTE", "OCCIDENTE"), ("OCCIDENTE", "BOSA"),
           ("BOSA", "SUR"), ("SUR", "VEREDA"), ("VEREDA", "CHAPINERO"),
           ("CHAPINERO", "USAQUEN"), ("USAQUEN", "ORIENTE"),
           ("CENTRO", "SUR")]                      # esta arista cierra un circuito

aristas_cortadas = [("CENTRO", "NORTE"), ("CENTRO", "SUR"), ("USAQUEN", "ORIENTE")]

def construir_lista(aristas):
    lst = [[] for _ in range(N)]
    for a, b in aristas:
        lst[idx[a]].append(idx[b])
        lst[idx[b]].append(idx[a])
    return lst

def dfs_iter(inicio, lista, visitado=None):
    if visitado is None:
        visitado = [False] * N
    pila = [inicio]
    orden = []
    while pila:
        u = pila.pop()                   # LIFO: sale el ultimo que entro
        if visitado[u]:
            continue                    
        visitado[u] = True
        orden.append(u)
        for v in reversed(lista[u]):    
            if not visitado[v]:
                pila.append(v)
    return orden

def componentes(lista):
    visitado = [False] * N
    comps = []
    for s in range(N):
        if not visitado[s]:
            comps.append(dfs_iter(s, lista, visitado))
    return comps

def tiene_circuito(lista):
    visitado = [False] * N
    for s in range(N):
        if visitado[s]:
            continue
        pila = [(s, -1)]              
        while pila:
            u, padre = pila.pop()
            if visitado[u]:
                continue
            visitado[u] = True
            for v in lista[u]:
                if visitado[v] and v != padre:
                    return True
            for v in reversed(lista[u]):
                if not visitado[v]:
                    pila.append((v, u))
    return False

def nombrar(ids):
    return [nombres[i] for i in ids]

lista = construir_lista(aristas)
print("DFS ITERATIVO (con pila explicita) desde CENTRO")
print("  orden de visita:", " -> ".join(nombrar(dfs_iter(idx["CENTRO"], lista))))
print()
print("COMPONENTES CONEXAS de la red completa:",
      [nombrar(c) for c in componentes(lista)])
lista_c = construir_lista(aristas_cortadas)
print("COMPONENTES de una red con tramos cortados:",
      [nombrar(c) for c in componentes(lista_c)])
print("¿La red tiene algun circuito?", tiene_circuito(lista))