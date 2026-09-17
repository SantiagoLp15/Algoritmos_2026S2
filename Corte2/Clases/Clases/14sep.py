# Fragmento 1
def factorial(n):
    return n * factorial(n-1)

# Fragmento 2
def suma(lista, i):
    if i >= len(lista):
        return 0
    return lista[i] + suma(lista, i+1)

# Fragmento 3
#La recursión es una función(subrutina) que si se presenta un problema, lo divide en subproblemas más pequeños y los resuelve de manera recursiva.
# Tiene caso base y caso recursivo, donde la función se llama a sí misma hasta llegar al caso base.
# La pila de llamadas trae cada caso recursivo para resolver el problema original.
camino [f][c] = 1
if resolver(f+1, c):
    return True
if resolver(f, c+1):
    return True
return False

def infinito(n):
    return infinito(n+1) #Nunca llega a un caso base, tiende a infinito.