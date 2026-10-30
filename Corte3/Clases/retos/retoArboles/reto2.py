#--------------------------------------
# Reto 2 arboles
#--------------------------------------
#El espejo Escriba espejo(nodo) que intercambie el hijo izquierdo 
#y el derecho de TODOS los nodos del árbol. 
#Luego imprima el inorden del árbol original y el del árbol espejado.
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
def espejo(nodo): # Ya no necesita los niveles, pues la original ya los asignó
    if nodo is None: return
    nodo.izq, nodo.der = nodo.der, nodo.izq
    espejo(nodo.izq)
    espejo(nodo.der)

if __name__ == "__main__":
    raiz = Nodo("Tecnología") # Nivel 0
    raiz.izq = Nodo("Laptops") # Nivel 1 izquierda
    raiz.der = Nodo("Celulares") # Nivel 1 derecha
    raiz.izq.izq = Nodo("MacBook") # Nivel 2 izquierda
    raiz.izq.izq = Nodo("Lenovo") # Nivel 2 izquierda
    raiz.der.der = Nodo("Apple") # Nivel 2 derecha
    raiz.der.der.der = Nodo("Iphone 17") # Nivel 3 derecha  
print("Resultado en orden:")
imprimir_arbol(raiz,0) 
print("Resultado en espejo:")
espejo(raiz)           # 1. Modifica el árbol invirtiendo sus ramas
imprimir_arbol(raiz, 0) # 2. Imprime el árbol ya modificado