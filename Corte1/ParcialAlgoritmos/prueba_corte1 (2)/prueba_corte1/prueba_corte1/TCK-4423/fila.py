# ============================================================
#  Cívica Software  ·  TCK-4423  ·  Severidad P0  ·  PRODUCCION CAIDA
#  Sistema: TurnoJusto  —  La fila de atencion pierde personas.
#
#  Reportes de soporte:
#   - "Atendi al primero de la fila y desaparecieron todos."
#   - "Retire a una persona del final y la fila sigue mostrandola."
#   - "La fila dice que tiene gente cuando esta vacia."
# ============================================================

class Nodo:
    def __init__(self, turno, nombre):
        #se definen los atributos de la clase Nodo
        self.turno = turno
        self.nombre = nombre
        self.siguiente = None
        #se define el atributo siguiente que apunta al siguiente nodo de la fila


class Fila:
    def __init__(self):
        self.cabeza = None
        #se define el atributo de la clase Fila que apunta al primer nodo de la fila

    def llegar(self, turno, nombre):
        #se define el metodo llegar que agrega un nodo al final de la fila
        """Agrega una persona al FINAL de la fila."""
        nuevo = Nodo(turno, nombre)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def retirar(self, turno):
        """Elimina de la fila a la persona con ese turno.
           Devuelve True si la elimino, False si no estaba.
           BUG P0: revise los tres casos."""
        if self.cabeza is None:
            #la fila esta vacia, no hay nadie que eliminar
            return False
        if self.cabeza.turno == turno:
            #el primer nodo de la fila es el que se quiere eliminar
            self.cabeza = self.cabeza.siguiente  # <-- caso 1


            return True
        
        anterior = self.cabeza
        while anterior.siguiente is not None:
            #confirma que haya un nodo siguiente al actual
            if anterior.siguiente.turno == turno:
                #se toma el nodo siguiente al actual
                anterior.siguiente = anterior.siguiente.siguiente  # <-- caso 2
                #se reemplaza el nodo siguiente al actual por el nodo siguiente al nodo que se quiere eliminar
                return True
            anterior = anterior.siguiente
        
        return False

    def cuantos(self):
        """Devuelve cuantas personas hay en la fila."""
        n = 0
        actual = self.cabeza
        while actual is not None:
            n += 1
            actual = actual.siguiente
        return n

    def listar(self):
        r = []
        actual = self.cabeza
        while actual is not None:
            r.append(actual.turno)
            actual = actual.siguiente
        return r
