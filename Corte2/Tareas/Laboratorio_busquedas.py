#----------------------------------
# PARTE A
#----------------------------------
#1. Insertion sort hace menos trabajo,
#pues como compara cada elemnto con el anterior,
# solo hace 999 comparaciones 

#2. El peor caso es un arreglo que ya esté ordenado, tal que:
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3. Sea N = 100000 y K = 100, entonces:
#Caso 1: Ordenamiento y busqueda binaria
#La cantidad de de veces que se compara es log2(10000) que es 13.3 y con 100 busquedas da 1330
# El ordenamiento es multiplocar la cantidad de busquedas por el numero de dados, es decir, hay 133000 operaciones
#En total, se llevan a cabo 134330 operaciones.
#Caso 2: Ordenamiento y busqueda secuencual 100 veces
#La cantidad de operaciones viene dada por K*(N/2)
#lo que da un total de 500000 operaciones
#En conclusion, es mejor si los ordeno y uso binaria.

#----------------------------------
# PARTE B
#----------------------------------
import random

# Cada recurso: (id, nombre, categoria, sede, cantidad)
# La búsqueda y el ordenamiento se hacen por el campo id (posición 0).
RECURSOS_ORDENADOS = [
    (101, "Salón",      "espacio",     "Norte",  1),
    (105, "Proyector",          "equipo",      "Centro", 2),
    (110, "Sillas",   "mobiliario",  "Sur",   80),
    (114, "Mesas",    "mobiliario",  "Norte", 20),
    (120, "Sonido",    "equipo",      "Centro", 1),
    (127, "Cancha múltiple",    "espacio",     "Sur",    1),
    (133, "Marcadores",          "equipo",      "Norte",  4),
    (140, "Sala en silencio", "espacio",     "Centro", 1),
    (146, "Computadores",       "equipo",      "Sur",   10),
    (152, "Portatil",       "equipo",      "Norte", 15),
]

def recursos_desordenados(semilla=1000):
    datos = list(RECURSOS_ORDENADOS)
    #Revuelve la lista
    random.Random(semilla).shuffle(datos)
    return datos

def generar_recursos(n, semilla=1000):
    rnd = random.Random(semilla)
    ids = rnd.sample(range(1, n * 10), n)
    cats = ["espacio", "equipo", "mobiliario", "transporte"]
    sedes = ["Norte", "Centro", "Sur"]
    return [(i, f"Recurso {i}", rnd.choice(cats), rnd.choice(sedes),
             rnd.randint(1, 50)) for i in ids]

if __name__ == "__main__":
    print(len(RECURSOS_ORDENADOS), "recursos de ejemplo")
    print(recursos_desordenados()[:3])
    print(len(generar_recursos(10000)), "recursos generados")
#----------------------------------
# PARTE F
#----------------------------------
#No estoy de acuerdo con la afirmación, pues a pesar que py no requeire compilación, CI si se necesita, 
#pues ayuda a revisar que el codigo funcione despuesd e cada edicion, lo que es necesario para cualquier lenguaje.

