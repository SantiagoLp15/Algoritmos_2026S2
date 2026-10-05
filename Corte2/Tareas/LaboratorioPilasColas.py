# ------------------------------------
#  PARTE A: COLA DE ATENCION
# ------------------------------------
# Crear clase nodo, que guarde el dato y tenga un puntero al siguiente.
class nodo:
    def __init__(self, dato): # Cada nodo incluye un dato y puntero
        self.dato = dato
        self.siguiente = None

# Crear una clase cola, donde se van a ordenar los nodos
class cola: 
    def __init__(self):
        self.inicio = None # Inicio de la cola, está vacia
        self.final = None # Fin de la cola, está vaacia
        self.tamaño = 0 # El tamaño de la cola inicia en 0
    def cola_vacia(self): # Función para saber si la cola tiene nodos
        return self.tamaño == 0
    def encolar(self, dato): # Función para agregar datos a la cola
        nuevo_nodo = nodo(dato) # Se crea un juevo nodo con el dato que se quiera agregar
        if self.cola_vacia():
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo # Se enlaza el nuevo nodo al que antes estaba al final
            self.final = nuevo_nodo
        self.tamaño += 1
    def desencolar(self): # Función para eliminar el dato del inicio
        if self.cola_vacia():
            print("ERROR: La cola está vacia")
            return None
        else:
            eliminar = self.inicio.dato
            self.inicio = self.inicio.siguiente # El nuevo dato del inicio es el siguiente.
            self.tamaño -= 1
            if self.cola_vacia():
                self.final = None
                print("Luego de eliminar el dato, la cola quedó vacia")
            return None
    def consultar_inicio(self): # Función que consulta el dato inicial
        if self.cola_vacia():
                print("ERROR: La cola está vacia")
                return None
        else: return self.inicio.dato
    def consultar_tamaño(self): # Funcion que consulta el tamaño de la cola
        if self.cola_vacia():
                        print("El tamaño es 0, la cola está vacia")
                        return self.tamaño
        else: return self.tamaño

# ------------------------------------
#  PARTE A: PRUEBA DE COLA
# ------------------------------------
# 1. Insertar clientes a la cola y verificar inicio y tamaño.
if __name__ == "__main__": 
    cola1 = cola()
    print("Han llegado cinco clientes al resinto y han pedido turno para ser atentidos.")
    cola1.encolar("Cliente 1")
    cola1.encolar("Cliente 2")
    cola1.encolar("Cliente 3")
    cola1.encolar("Cliente 4")
    cola1.encolar("Cliente 5")
    print(f"Al inicio de la cola está: {cola1.consultar_inicio()}")
    print(f"El tamaño de la cola es: {cola1.consultar_tamaño()}")
# 2. Desencolar clientes y verificar nuevamente inicio y tamaño.
    print("Se ha terminado de atenter al Cliente 1, por lo que el siguiente puede seguir con su turno.")
    cola1.desencolar() # Se elimino el primer elemento de la cola, ahora quedan 4.
    print(f"Al inicio de la cola está: {cola1.consultar_inicio()}")
    print(f"El nuevo tamaño de la cola es: {cola1.consultar_tamaño()}")
# 3. Eliminar todos los clientes y verificar que la cola esté vacia.
    print("Todos los clientes han sido atendidos, es hora de almuerzo")
    cola1.desencolar() # Se elimino el segundo elemento de la cola, ahora quedan 4.
    cola1.desencolar() # Se elimino el tercer elemento de la cola, ahora quedan 2.
    cola1.desencolar() # Se elimino el cuarto elemento de la cola, ahora quedan 1.
    cola1.desencolar() # Se elimino el quinto elemento de la cola, ahora quedan 0.
    print(f"Al inicio de la cola está: {cola1.consultar_inicio()}")
    print(f"El nuevo tamaño de la cola es: {cola1.consultar_tamaño()}")
    print(f"¿La cola está vacia?: {cola1.cola_vacia()}")
# 4. Agregar nuevos clientes a la cola y verificar el inicio y tamaño.
    print("Terminada la hora de almuerzo, llegaron dos clientes nuevos.")
    cola1.encolar("Cliente 6")
    cola1.encolar("Cliente 7")
    print(f"Al inicio de la cola está: {cola1.consultar_inicio()}")
    print(f"El tamaño de la cola es: {cola1.consultar_tamaño()}")

# -------------------------------------------
#  PARTE B: DESHACER COMPRA DE ACCIONES
# -------------------------------------------
# Crear una cuenta de inversión, con saldo inicial y que permita operar entre cinco acciones.
# Cada operación (compra/venta) se guarda en una pila
# deshacer revierte el saldo y composición del portafolio, no solo borra el registro.

class pila: #Pila (LIFO) para registrar las últimas operaciones.
    def __init__(self):
        self.items = []
    def push(self, elemento):
        self.items.append(elemento)
    def pop(self):
        if self.esta_vacia():
            return None
        return self.items.pop()
    def peek(self):
        if self.esta_vacia():
            return None
        return self.items[-1]
    def esta_vacia(self):
        return len(self.items) == 0
    def __len__(self):
        return len(self.items)
    
class acciones:
    def __init__(self, nombre: str, precio: float): # Los componentes de una accion son el nombre y el precio del mercado
        self.nombre = nombre
        self.precio = precio

class operacion: # La operacion necesita conocer cantidad, precio y si es compra o venta
    def __init__(self, accion: acciones, cantidad: float, tipo: bool, precio_accion: float):
        self.accion = accion
        self.cantidad = cantidad
        self.tipo = tipo  # True = compra, False = venta
        self.precio_accion = precio_accion  # precio al momento de la operación
        self.monto = cantidad * precio_accion # Monto total de la operación

    def _datos_validos(self):
        # Solo son validos cuando la cantidad y precioson positivos
        if self.cantidad > 0 and self.precio_accion > 0: return self._datos_validos

    def compra(self):
        if not self._datos_validos(): # Comprobar que los datos sean validos
            print("ERROR: Los datos ingresados no son validos")
            return None
        return self.monto # En caso de que sean validos

    def venta(self):
        if not self._datos_validos():
            print("ERROR: Los datos ingresados no son validos")
            return None
        return self.monto

    def __str__(self):
        nombre_tipo = "COMPRA" if self.tipo else "VENTA"
        return f"{nombre_tipo} {self.cantidad} x {self.accion.nombre} @ {self.precio_accion} = {self.monto}"


class portafolio:
    def __init__(self, saldo: float, lista_acciones: list):
        self.saldo = saldo
        self.acciones = {a.nombre: a for a in lista_acciones}  # catálogo de cinco acciones
        self.tenencias = {a.nombre: 0 for a in lista_acciones}  # cantidad de acciones de cada una
        self.historial = pila()  # pila de operaciones para deshacer

    def calcular_total(self):
        # Valor total = saldo en efectivo + valor de las acciones a precio actual
        total = self.saldo
        for nombre, cantidad in self.tenencias.items():
            total += cantidad * self.acciones[nombre].precio
        return total

    def comprar(self, nombre: str, cantidad: int):
        if nombre not in self.acciones:
            print("La accion no existe")
            return False
        accion = self.acciones[nombre]
        op = operacion(accion, cantidad, True, accion.precio)
        monto = op.compra()
        if monto is None:
            return False
        if monto > self.saldo:
            print("Saldo insuficiente")
            return False
        self.saldo -= monto
        self.tenencias[nombre] += cantidad
        self.historial.push(op)
        return True

    def vender(self, nombre: str, cantidad: int):
        if nombre not in self.acciones:
            print("La accion no existe")
            return False
        accion = self.acciones[nombre]
        op = operacion(accion, cantidad, False, accion.precio)
        monto = op.venta()
        if monto is None:
            return False
        if cantidad > self.tenencias[nombre]:
            print("No tienes suficientes acciones para vender")
            return False
        self.saldo += monto
        self.tenencias[nombre] -= cantidad
        self.historial.push(op)
        return True

    def deshacer(self):
        """Revierte la última operación: ajusta saldo y tenencias de verdad."""
        op = self.historial.pop()
        if op is None:
            print("No hay operaciones para deshacer")
            return False
        nombre = op.accion.nombre
        if op.tipo:  # se deshace una compra: devuelve el dinero y quita las acciones
            self.saldo += op.monto
            self.tenencias[nombre] -= op.cantidad
        else:  # se deshace una venta: quita el dinero y devuelve las acciones
            self.saldo -= op.monto
            self.tenencias[nombre] += op.cantidad
        print("Deshecho:", op)
        return True


# -------------------------------------------
#  PRUEBA
# -------------------------------------------
def prueba():
    catalogo = [
        acciones("AAPL", 100.0),
        acciones("MSFT", 200.0),
        acciones("TSLA", 50.0),
        acciones("AMZN", 150.0),
        acciones("NVDA", 300.0),
    ]
    p = portafolio(10000.0, catalogo)
    assert p.calcular_total() == 10000.0

    # 1) Compra y deshacer compra
    assert p.comprar("AAPL", 10)  # -1000
    assert p.saldo == 9000.0 and p.tenencias["AAPL"] == 10
    p.deshacer()
    assert p.saldo == 10000.0 and p.tenencias["AAPL"] == 0

    # 2) Varias operaciones y deshacer en orden inverso (LIFO)
    p.comprar("MSFT", 5)   # -1000 -> 9000
    p.comprar("TSLA", 20)  # -1000 -> 8000
    p.vender("MSFT", 2)    # +400  -> 8400
    assert p.saldo == 8400.0
    assert p.tenencias["MSFT"] == 3 and p.tenencias["TSLA"] == 20

    p.deshacer()  # deshace la venta de MSFT
    assert p.saldo == 8000.0 and p.tenencias["MSFT"] == 5
    p.deshacer()  # deshace la compra de TSLA
    assert p.saldo == 9000.0 and p.tenencias["TSLA"] == 0
    p.deshacer()  # deshace la compra de MSFT
    assert p.saldo == 10000.0 and p.tenencias["MSFT"] == 0

    # 3) Pila vacía
    assert p.deshacer() is False

    # 4) Validaciones
    assert p.comprar("NVDA", 0) is False       # cantidad inválida
    assert p.comprar("NVDA", 1000) is False    # saldo insuficiente
    assert p.vender("AMZN", 1) is False        # no tiene acciones
    assert p.comprar("XXXX", 1) is False       # acción inexistente
    assert len(p.historial) == 0               # las operaciones fallidas no se registran

    # 5) El deshacer usa el precio de la operación, aunque el precio actual cambie
    p.comprar("NVDA", 10)                      # -3000 a precio 300
    catalogo[4].precio = 400.0                 # sube el precio
    p.deshacer()
    assert p.saldo == 10000.0                  # se devuelve exactamente lo pagado

    print("\nTodas las pruebas pasaron correctamente")


if __name__ == "__main__":
    prueba()

    
             
              
        
     
     
