# Sesion 40 — Grafos: matriz de adyacencia frente a lista de adyacencia

NOMBRES = ["centro", "norte", "occidente", "chapinero", "sur",
           "bosa", "oriente", "usaquen", "vereda"]
N = len(NOMBRES)
indice = {nombre: i for i, nombre in enumerate(NOMBRES)}

VIAS = """
centro - norte
norte - occidente
norte - chapinero
sur - bosa
oriente - usaquen
chapinero - usaquen
occidente - bosa
bosa - vereda
vereda - norte
bosa - chapinero
chapinero - vereda
sur - usaquen
usaquen - vereda
norte - vereda
chapinero - bosa
chapinero - sur
"""

# Se convierte el texto en pares (u, v) y se eliminan las vias repetidas, tal que vereda-norte y norte-vereda son la misma via
vistas = set()
ARISTAS = []
for linea in VIAS.strip().splitlines():
    a, b = (x.strip() for x in linea.split("-")) # Divide la linea en dos partes separadas por el guion.
    u, v = indice[a], indice[b] # Convierte los nombres en inndices
    clave = frozenset((u, v)) # elimina el orden para que no hayan vias repetidas
    if clave not in vistas: # evalua si la via ya fue agregada.
        vistas.add(clave) # añade la via a la lista.
        ARISTAS.append((u, v))

# ---------- Representacion 1: matriz de adyacencia ----------
matriz = [[0]*N for _ in range(N)]
for u, v in ARISTAS:
    matriz[u][v] = 1
    matriz[v][u] = 1              # no dirigido: matriz simetrica

print("MATRIZ DE ADYACENCIA")
print("            " + " ".join(f"{n[:3]:>4}" for n in NOMBRES))
for i in range(N):
    print(f"{NOMBRES[i]:>11} " + " ".join(f"{matriz[i][j]:>4}" for j in range(N)))

# ---------- Representacion 2: lista de adyacencia ----------
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)
    lista[v].append(u)
for v in lista: v.sort()

print("\nLISTA DE ADYACENCIA")
for i in range(N):
    print(f"  {NOMBRES[i]:>10} -> {', '.join(NOMBRES[j] for j in lista[i])}")

# ---------- Grados ----------
print("\nGRADO DE CADA VERTICE (cuantas vias salen de el)")
for i in range(N):
    g_mat = sum(matriz[i])        # recorre una fila: O(N)
    g_lis = len(lista[i])         # lee el tamaño: O(1)
    assert g_mat == g_lis
    print(f"  {NOMBRES[i]:>10}: {g_lis}")

# ---------- Costos ----------
aristas = len(ARISTAS)
print(f"\nV = {N} vertices,  E = {aristas} aristas")
print(f"  Matriz : {N*N} casillas en memoria. ¿Existe arista? O(1). Recorrer vecinos: O(V) = {N} casillas.")
print(f"  Lista  : {2*aristas} referencias en memoria. ¿Existe arista? O(grado). Recorrer vecinos: O(grado).")
densidad = 2*aristas / (N*(N-1))
print(f"  Densidad = 2E / (V(V-1)) = {densidad:.2f}  ->  grafo {'DENSO: conviene matriz' if densidad > 0.5 else 'DISPERSO: conviene lista'}")

# ---------- Consulta de arista: Chapinero contra las otras 8 localidades ----------
# Toma Chapinero como u, si está contectado con v, returna True.
def hay_via_matriz(u, v): return matriz[u][v] == 1 # Da 1 cuando hay conexion y 0 cuando no hay.
def hay_via_lista(u, v):  return v in lista[u]

yo = indice["chapinero"]
print()
for v in range(N):
    if v == yo:
        continue
    print(f"  ¿{NOMBRES[yo].upper()} conecta con {NOMBRES[v].upper()}? "
          f"matriz={hay_via_matriz(yo, v)}  lista={hay_via_lista(yo, v)}")