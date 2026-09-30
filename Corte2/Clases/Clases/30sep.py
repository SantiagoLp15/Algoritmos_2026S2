#----------------------------------
# PILAS Y COLAS
#----------------------------------

#----------------------------------
# PILAS (STACK)
#----------------------------------
# Estructura tipo LIFOc (ultimo que entra, primero que sale)
# Solo accede a los elementos de los extremos o topes, las operaciones son:
# push(x): Colocar en el tope
# pop(): elimina el elemento del tope
# peek(): ver el elemento del tope
# is_empty: verifica si la pila está vacia
# size: tamaño de la pila
# top() : obtener el tope de la fila
# Las pilas tiene tres funciones: Apilar, desapilar y cima (ver el tope). Todas son O(1)
# Si apilo sobre arr se apila al final
# Si apilo sobre una lista enlazada, apilo al inicio

class Pila:
    def __init__(self):self.items = []
    def apilar(self,x):self.items.append(x)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):return len(self.items) == 0
    #apilar sobre un array apilo al final O(1) sobre una 
    # lista enlazada apilo al inicio O(1) 
    # desapilar sobre un array desapilo al final O(1) 
    # sobre una lista enlazada desapilo al inicio O(1)
    
    # (a[b]{c}) y (a[b)c] pila cada vez 
    # que se abre un corchete o paréntesis se apila 
    # y cada vez que se cierra se desapila 
    # y se compara con el tope de la pila 
    # si es igual se desapila sino no es balanceado
    
    def balanceados(s):
        p=Pila(); pares={')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{': p.apilar(c)
            elif c in ')]}':
                if p.desapilar() != pares[c]: return False
        return p.vacia()
    
    print(balanceados("()"))
    print(balanceados("([]{})"))
    print(balanceados("([)]"))
    print(balanceados("((())"))

    #(a[b]{c})
    #([)]
    #((()
    #{}[]()