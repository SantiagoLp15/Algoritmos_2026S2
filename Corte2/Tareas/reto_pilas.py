class Nodo:
    """Un eslabón de la cadena: guarda un dato y apunta al siguiente nodo."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:

    def __init__(self):
        self.tope = None      # nodo de arriba de la pila
        self._cantidad = 0    # contador para size(), inicia en 0

    def esta_vacia(self): # fuincion si la pila está vacia
        return self.tope is None # como está vacia no hay tope

    def apilar(self, dato): # definir funcion push: pone eleemnto en el tope 
        nodo_nuevo = Nodo(dato)
        nodo_nuevo.siguiente = self.tope   # el nuevo apunta al que era tope
        self.tope = nodo_nuevo             # el nuevo pasa a ser el tope
        self._cantidad += 1                # el tamaño aumenta en uno

    def desapilar(self): # función pop: quita el tope t devuelve el dato
        if self.esta_vacia(): # en caso de que la pila esté vacia
            raise IndexError("No se puede desapilar: la pila está vacía")
        nodo_quitado = self.tope # el nodo a eliminar es el del tope
        self.tope = self.tope.siguiente    # el segundo nodo pasa a ser tope
        self._cantidad -= 1 # el tamaño de la pila se reduce en uno
        return nodo_quitado.dato # devuelve el nodo que fue eliminado 

    def ver_tope(self): # funcion peek: imprime el dato tope
        if self.esta_vacia(): # en caso de que la pila esté vacia
            raise IndexError("La pila está vacía")
        return self.tope.dato # devuelve el dato ubicado en el tope

    def tamano(self): # funcion para hallar el tamaño de la pila
        return self._cantidad

    def __str__(self): # muestra la pila desde el tope hasta el final
        elementos = [] # la lista inicia vacia
        actual = self.tope # actual es el dato del tope
        while actual is not None: # evalua qye la pila no esté vacia y si haya dato en el tope
            elementos.append(str(actual.dato)) # agrega el dato del tope a elementos
            actual = actual.siguiente # el nuevo dato a agregar es el siguiente, repitiendo el ciclo hasta no tener datos 
        return "Tope -> " + " -> ".join(elementos) if elementos else "Pila vacía" # Devuelve elementos en orden, en caso de que no hayan imprime Pila vacia


if __name__ == "__main__":
    p = Pila() # almacena los datos en la pila vacia
    print("¿Vacía?", p.esta_vacia()) # evalua si la pila está vacia

    p.apilar(10) #datos a apilar
    p.apilar(20) #datos a apilar
    p.apilar(30) #datos a apilar
    print(p)                    # Tope -> 30 -> 20 -> 10
    print("Tamaño:", p.tamano())

    print("Tope actual:", p.ver_tope())   # 30, sin quitarlo
    print("Desapilado:", p.desapilar())   #  imprime y elimina el tope (20)
    print(p)                              # Tope -> 20 -> 10, pues se eliminó el tope anterior

    print("Desapilado:", p.desapilar())   # imprime y elimina el tope (20)
    print("Desapilado:", p.desapilar())   # imprime y elimina el tope (10)
    print("¿Vacía?", p.esta_vacia()) # evalua si la pila está vacia

