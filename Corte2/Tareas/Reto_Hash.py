

# 1. Definir clase para la tabla hash
class tabla_hash:
    def __init__(self, capacidad=8): # Capacidad de 8
        self.cap = capacidad
        self.cubetas = [[] for _ in range(self.cap)] # Lista de cubetas vacia
        self.n = 0 # n es un contados de la cantidad de elementos guardados

    # Funcion hash: convierte la clave en un numero para asignar la cubeta
    def tabla_hash(self, clave):
        h = 0 # Contador inicia en 0
        for c in str(clave): # Recorre cada carcarter de la clave en texto
            h = (h * 31 + ord(c)) % self.cap # conversion numerica para obtener el indice
        return h # retorna el indice obtenido

    # Funcion para calcula el factor de carga: elementos(n) / capacidad(m)
    def factor_carga(self):
        return self.n / self.cap

    # Funcion para redimensionar 
    def redimensionar(self):
        # Se guardan los datos de las cubetas viejas
        viejas = self.cubetas
        # Se duplica la capacidad(m)
        self.cap = self.cap * 2
        # Se crean nuevas cubetas, todas estan vacias por ende n = 0
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0
        # Se corre las cubetas viejas
        for cubeta in viejas:
            for clave, valor in cubeta:
                    # Se insertan los valores viejos en la nueva tabla
                self.insertar(clave, valor)

    # Funcion para insertar en cubeta
    def insertar(self, clave, valor):
        indice = self.tabla_hash(clave)
        # Recorremos la cubeta con posicion
        for i, (k, v) in enumerate(self.cubetas[indice]):
            # Si la clave ya existe
            if k == clave:
                # Se actualiza el valor
                self.cubetas[indice][i] = (clave, valor)
                return
        # Si la clave no existe, se agrega al final de la cubeta
        self.cubetas[indice].append((clave, valor))
        # Aumenta el contador de elementos(n)
        self.n += 1
        # Si el factor de carga supera los 0.75
        if self.factor_carga() > 0.75:
            # se redimensiona la tabla
            self.redimensionar()

    # Funcion para buscar una clave
    def buscar(self, clave):
        # Hallar la cubeta donde deberia estar
        indice = self.tabla_hash(clave)
        # Recorrer esa cubeta
        for k, v in self.cubetas[indice]:
            # Si se encuentran los valores
            if k == clave:
                # Se retorna el valor
                return v
        # Si no se encuentran, se devuelve None
        return None

    # Funcion para imrpimir la tabla
    def mostrar(self):
        # Recorre cada cubeta con su indice
        for i, cubeta in enumerate(self.cubetas):
            # Imprime el indice y el contenido de la cubeta
            print(i, ":", cubeta)

# -------------------------------
# PRUEBA
# -------------------------------

# Lista con 12 estudiantes
estudiantes = [
    ("EST-2026-0101", "Ana Torres"),
    ("EST-2026-0102", "Carlos Rojas"),
    ("EST-2026-0103", "Diego Pardo"),
    ("EST-2026-0104", "Sofia Mejia"),
    ("EST-2026-0105", "Juan Gomez"),
    ("EST-2026-0106", "Maria Lopez"),
    ("EST-2026-0107", "Pedro Ruiz"),
    ("EST-2026-0108", "Camila Diaz"),
    ("EST-2026-0109", "Luis Herrera"),
    ("EST-2026-0110", "Valentina Cruz"),
    ("EST-2026-0111", "Andres Vega"),
    ("EST-2026-0112", "Laura Castro"),
]

# Crear la tabla
tabla = tabla_hash(8)

# Insertar cada estudiante a la tabla
for codigo, nombre in estudiantes:
    tabla.insertar(codigo, nombre)

# Imprimir la tabla final
tabla.mostrar()

# Imprimir la capacidad final, la cantidad de elementos y el factor de carga
print("Capacidad final:", tabla.cap)
print("Elementos:", tabla.n)
print("Factor de carga:", tabla.factor_carga())

# Busqueda del estudiante EST-2026-0107
print("Busqueda EST-2026-0107:", tabla.buscar("EST-2026-0107"))

# Busqueda de un codigo que no existe 
print("Busqueda EST-2026-0999:", tabla.buscar("EST-2026-0999"))