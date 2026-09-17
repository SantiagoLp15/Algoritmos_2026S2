#La recursión es una función(subrutina) que si se presenta un problema, lo divide en subproblemas más pequeños y los resuelve de manera recursiva.
# Tiene caso base y caso recursivo, donde la función se llama a sí misma hasta llegar al caso base.
# La pila de llamadas trae cada caso recursivo para resolver el problema original.
nivel = 0

def factorial(n):
    global nivel
    print("|  " * nivel + f"factorial({n}) entra")
    nivel += 1
    r = 1 if n <= 1 else n * factorial(n - 1)
    nivel -= 1
    print("|  " * nivel + f"factorial({n}) devuelve {r}")
    return r

def fibonacci(m):
    if m <= 1:
        return m
    return fibonacci(m - 1) + fibonacci(m - 2)

print("--- traza de la pila de llamadas ---")
n = 4
m = 10
r = factorial(n)
print("Resultado:", r)
print()
print("fibonacci =", fibonacci(m))
def calcular_tiempo_fibonacci(m):
    import time
    start_time = time.time()
    result = fibonacci(m)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time
print("El resultado y tiempo fue:", calcular_tiempo_fibonacci(m))
