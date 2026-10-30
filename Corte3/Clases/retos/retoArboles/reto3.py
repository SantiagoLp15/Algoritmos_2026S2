#--------------------------------------
# Reto 2 arboles
#--------------------------------------
#Escriba sonIguales(a, b) que devuelva verdadero si tienen la misma forma
# Y los mismos datos en las mismas posiciones. 
# Pruébelo con el árbol original contra su propio espejo: debe dar falso.

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
def prueba_igualdad(a, b):
    # 1. Si ambos son none al final, esta rama es igual
    if a is None and b is None:
        return True
    
    # 2. Si uno es None y el otro no, tienen formas distintas
    if a is None or b is None:
        return False
    
    # 3. Si el valor actual coincide, se verifican los hijos 
    if a.valor == b.valor:
        return prueba_igualdad(a.izq, b.izq) and prueba_igualdad(a.der, b.der)
    
    # 4. Si los valores son diferentes
    return False
if __name__ == "__main__":
    # Arbol original
    raiz = Nodo("Tecnología") # Nivel 0
    raiz.izq = Nodo("Laptops") # Nivel 1 izquierda
    raiz.der = Nodo("Celulares") # Nivel 1 derecha
    raiz.izq.izq = Nodo("MacBook") # Nivel 2 izquierda
    raiz.izq.izq = Nodo("Lenovo") # Nivel 2 izquierda
    raiz.der.der = Nodo("Apple") # Nivel 2 derecha
    raiz.der.der.der = Nodo("Iphone 17") # Nivel 3 derecha  
    # Arbol espejo
    raiz_espejo = Nodo("Tecnología")
    raiz_espejo.izq = Nodo("Laptops")
    raiz_espejo.der = Nodo("Celulares")
    raiz_espejo.izq.izq = Nodo("Lenovo")
    raiz_espejo.der.der = Nodo("Apple")
    raiz_espejo.der.der.der = Nodo("Iphone 17")
    espejo(raiz_espejo) # # Ahora hay un segundo arbol que es espejo
print("Resultado en orden:")
imprimir_arbol(raiz,0) 
print("Resultado en espejo:")
espejo(raiz)           # 1. Modifica el árbol invirtiendo sus ramas
imprimir_arbol(raiz, 0) # 2. Imprime el árbol ya 
print("¿Son iguales el original y su espejo?")
resultado = prueba_igualdad(raiz, raiz_espejo)
print(f"¿Son iguales?: {resultado}")