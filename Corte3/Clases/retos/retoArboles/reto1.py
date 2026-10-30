#--------------------------------------
# Reto 1 arboles
#--------------------------------------
#El catálogo que se imprime solo Escriba una función imprimirJerarquia(nodo, nivel) 
# que recorra el árbol en preorden e imprima cada nombre con dos espacios de sangría por nivel, 
# de modo que el resultado se vea como un índice de documento. Debe funcionar para cualquier árbol, 
# no solo para el del ejemplo.

class Nodo:
    def __init__(self, valor):
        self.valor = valor    
        self.izq = None       # Apunta al hijo del lado izquierdo (al inicio no tiene)
        self.der = None       # Apunta al hijo del lado derecho (al inicio no tiene)
def imprimir_arbol(nodo, nivel=0):
    if nodo is None: return # Se evalua que el nodo tenga información
     # Imprime el nivel cero, la raiz
    print(" "*nivel+str(nodo.valor))
    # Imprime el primer nivel, primero visita la izquierda
    imprimir_arbol(nodo.izq, nivel +1)
    # Imprime el primer nivel pero ahora evalua el lado derecho
    imprimir_arbol(nodo.der, nivel+1)

# --- PRUEBA DEL CÓDIGO ---
if __name__ == "__main__":
    raiz = Nodo("Tecnología") # Nivel 0
    raiz.izq = Nodo("Laptops") # Nivel 1 izquierda
    raiz.der = Nodo("Celulares") # Nivel 1 derecha
    raiz.izq.izq = Nodo("MacBook") # Nivel 2 izquierda
    raiz.izq.izq = Nodo("Lenovo") # Nivel 2 izquierda
    raiz.der.der = Nodo("Apple") # Nivel 2 derecha
    raiz.der.der.der = Nodo("Iphone 17") # Nivel 3 derecha
    
    print("Resultado del Reto 1:")
    imprimir_arbol(raiz,0)