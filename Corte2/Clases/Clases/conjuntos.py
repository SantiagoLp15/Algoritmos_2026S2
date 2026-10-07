#------------------------------------
# CONJUNTOS
#------------------------------------
# Es como una lista pero mas rapida
# Guarda elementos sin repeticion ni orden
#------------------------------------
# MAPA
#------------------------------------
# Guarda elementos sin repeticion pero en orden
a = {"papel", "lapiz", "cuaderno"}
b = {"vidrio", "madera", "papel"}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

#------------------------------------
# FUNCION HASH
#------------------------------------
# Convierte un elemento en numero entero
# Determinista: La misma clave da el mismo resultado (valor, posicion)
# Bien dividida

clave = 123
def hash(self, elemento):
    h = 0
    for c in str(clave):
        h = (h*31+ord(c))%100
    return h

# Diversionamento: cuando dos elementos tienen mismo valor, un elemento se guarda en la siguiente cubeta (espacio)
# Factor de carga: cantidad de elementos vs cantidad de cubetas(espacios), tal que: n(elementos)/m(cubetas)
# cuando es <= a 0.5, no hya tanatas colisiones, en el caso contrario (>= .5) hay mas
# Redimension: cuando >0.75, las cuebtas se duplicand, esto se llama re-hash
