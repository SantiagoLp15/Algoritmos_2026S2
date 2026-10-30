class Nodo:
    def __init__(self, c):
        self.clave = c; self.izq = None; self.der = None; self.alt = 0

def alt(n):  return -1 if n is None else n.alt
def fe(n):   return 0 if n is None else alt(n.izq) - alt(n.der)
def recalc(n): n.alt = 1 + max(alt(n.izq), alt(n.der))

def rotarDerecha(y):
    x = y.izq; B = x.der
    x.der = y; y.izq = B
    recalc(y); recalc(x)
    return x

def rotarIzquierda(x):
    y = x.der; B = y.izq
    y.izq = x; x.der = B
    recalc(x); recalc(y)
    return y

def inorden(n, s):
    if n is None: return
    inorden(n.izq, s); s.append(n.clave); inorden(n.der, s)

def preorden(n, s):
    if n is None: return
    s.append(f"{n.clave}(fe={fe(n)})"); preorden(n.izq, s); preorden(n.der, s)

def ver(titulo, raiz):
    s = []; preorden(raiz, s)
    t = []; inorden(raiz, t)
    print(f"{titulo:22s} preorden: {' '.join(s)}")
    print(f"{'':22s} inorden: {t} altura={alt(raiz)}")

# Insercion BST normal: NO balancea, solo actualiza alturas al volver
def insertar(n, c):
    if n is None: return Nodo(c)
    if c < n.clave:   n.izq = insertar(n.izq, c)
    elif c > n.clave: n.der = insertar(n.der, c)
    recalc(n)
    return n

# Diagnostico: solo necesita fe(nodo) y fe(hijo del lado pesado)
def diagnosticar(r):
    f = fe(r)
    if -1 <= f <= 1:
        return "OK"
    if f > 1:                                  # pesado a la izquierda
        return "LL" if fe(r.izq) >= 0 else "LR"
    return "RR" if fe(r.der) <= 0 else "RL"    # pesado a la derecha

def balancear(r, caso):
    if caso == "LL":
        return rotarDerecha(r)
    if caso == "RR":
        return rotarIzquierda(r)
    if caso == "LR":
        r.izq = rotarIzquierda(r.izq); recalc(r)
        ver("tras rotar el hijo", r)
        return rotarDerecha(r)
    if caso == "RL":
        r.der = rotarDerecha(r.der); recalc(r)
        ver("tras rotar el hijo", r)
        return rotarIzquierda(r)
    return r

claves = [int(x) for x in input("Claves tal que (30 10 20):").split()]
r = None
for c in claves:
    r = insertar(r, c)

caso = diagnosticar(r)
print(f"\nfe raiz = {fe(r)}", end="")
if caso != "OK":
    hijo = r.izq if fe(r) > 0 else r.der
    print(f", fe hijo pesado = {fe(hijo)}", end="")
print(f"  ->  caso: {caso}\n")

ver("antes", r)
r = balancear(r, caso)
ver("despues", r)