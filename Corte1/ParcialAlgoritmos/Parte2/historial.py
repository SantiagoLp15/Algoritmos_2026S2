# ============================================================
#  Cívica Software  ·  TCK-5512  ·  Severidad P0  ·  PRODUCCION CAIDA
#  Sistema: TurnoJusto  —  El historial de atenciones esta corrupto.
#
#  Reportes de soporte:
#   - "Registre la primera atencion del dia y el sistema se cayo."
#   - "Deshice la ultima atencion y se borro todo el historial."
#   - "Busco un turno que si existe y me dice que no esta."
# ============================================================

class Nodo:
    def __init__(self, turno, modulo):
        self.turno = turno
        self.modulo = modulo
        self.siguiente = None


class Historial:
    def __init__(self):
        self.cabeza = None

    def registrar(self, turno, modulo):
        """Agrega una atencion al FINAL del historial.
           BUG: se cae cuando el historial esta vacio."""
        nuevo = Nodo(turno, modulo)
        # Se usa if para comprobar si no hay la cabeza, en ese caso se asigna el nuevo nodo como cabeza.
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza                  # <-- ¿que pasa si no hay cabeza?
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    
    def deshacer_ultima(self):
        """Elimina la ULTIMA atencion registrada.
           Devuelve True si elimino algo, False si el historial estaba vacio.
           BUG: borra todo el historial."""
        # Comprobar que haya cabeza, si no hay retorna flase.
        if self.cabeza is None:
            return False
        # Si solo hay un dato, se elimina la cabeza y se retorna True.
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return True
        # Si hay mas de un dato,se recorre la lista hasta el penultimo.
        actual = self.cabeza
        # verifica que haya un ultimo datos.
        while actual.siguiente.siguiente is not None:
            # Reemplaza el dato actual por el siguiente, hasta el penultimo.
            # Es la mejor solución ya que ahorra lineas de código y es más eficiente que recorrer la lista manualmente.
            actual = actual.siguiente
        actual.siguiente = None
        return True

    def buscar(self, turno):
        """Devuelve el modulo que atendio ese turno, o None si no existe.
           PENDIENTE: implementar."""
        # Se recorre toda la lista de datos.
        actual = self.cabeza
        # Se hace un bucle para recorrer la lista con while.
        # While es la mejor herramienta ya que recorre la lista en bucle hasta que se encuentre el dato o se acabe la lista, sin necesidad de lienas extra.
        while actual is not None:
            # Se compara el dato actual con el dato buscado.
            if actual.turno == turno:
                # Si es igual, se retorna el modulo que atendio ese turno.
                return actual.modulo
            # Si no es igual, se pasa al siguiente dato.
            actual = actual.siguiente
        # Si no se encuentra el dato, se retorna None.    
        return None


    def cuantas(self):
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
