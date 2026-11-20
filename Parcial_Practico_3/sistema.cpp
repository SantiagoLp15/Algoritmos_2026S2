#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include "sistema.h"
using namespace std;

// ============================================================
//   BASE YA RESUELTA — lea estas funciones: son su punto de partida
//   y muestran el estilo con el que debe escribir las que faltan.
//   En la mesa se le puede preguntar por cualquiera de ellas.
// ============================================================

Punto::Punto(int c, const string& n, int cantidad) {
    codigo = c;
    nombre = n;
    nm = cantidad;
    mediciones = new int[nm];              // memoria dinamica
    for (int i = 0; i < nm; i++) mediciones[i] = 0;
    sig = nullptr;
}

int Punto::total() const {
    int s = 0;
    for (int i = 0; i < nm; i++) s += mediciones[i];
    return s;
}
// CLAVE PARA EL PARCIAL: apunta al mismo Punto que està en la lista
NodoIndice::NodoIndice(int c, Punto* p) {
    codigo = c; dato = p; izq = nullptr; der = nullptr;
}

Sistema::Sistema(int capacidadCola, const vector<pair<int,int>>& vias, int vertices) {
    lista  = nullptr;
    indice = nullptr;
    cap    = capacidadCola;
    cola   = new int[cap];
    frente = 0;
    enCola = 0;
    aristas = vias;
    red.assign(vertices, {});
    for (size_t i = 0; i < vias.size(); i++) {
        red[vias[i].first ].push_back(vias[i].second);
        red[vias[i].second].push_back(vias[i].first);
    }
    for (size_t i = 0; i < red.size(); i++) sort(red[i].begin(), red[i].end());
}

Sistema::~Sistema() {
    liberarTodo();                         // usted escribe liberarTodo()
    delete[] cola;
}

bool Sistema::encolar(int codigo) {
    if (enCola == cap) return false;                 // desbordamiento controlado
    cola[(frente + enCola) % cap] = codigo;          // el final se CALCULA
    enCola++;
    return true;
}

bool Sistema::siguiente(int& codigo) {
    if (enCola == 0) return false;                   // subdesbordamiento
    codigo = cola[frente];
    frente = (frente + 1) % cap;
    enCola--;
    return true;
}

string Sistema::enEspera() const {
    string r;
    for (int i = 0; i < enCola; i++) {
        if (i > 0) r += " ";
        r += to_string(cola[(frente + i) % cap]);
    }
    return r;
}

int Sistema::cuantos() const {
    int k = 0;
    for (Punto* a = lista; a != nullptr; a = a->sig) k++;
    return k;
}

string Sistema::codigos() const {
    string r;
    for (Punto* a = lista; a != nullptr; a = a->sig) {
        if (!r.empty()) r += " ";
        r += to_string(a->codigo);
    }
    return r;
}

void Sistema::medir(int codigo, int i, int valor) {
    Punto* p = buscar(codigo);                       // usa SU buscar()
    if (p == nullptr) return;
    if (i < 0 || i >= p->nm) return;                 // indice fuera de rango
    p->mediciones[i] = valor;
}

int Sistema::sumaTotales() const {
    int s = 0;
    for (Punto* a = lista; a != nullptr; a = a->sig) s += a->total();
    return s;
}
// ------------------------------------------------------------
//   Estas cinco funciones TAMBIEN se le entregan resueltas.
//   Lealas: son el modelo de lo que usted debe escribir, y en la
//   mesa se le puede preguntar por cualquiera de ellas.
// ------------------------------------------------------------


Punto* Sistema::buscar(int codigo) const {
    NodoIndice* n = indice;                 // DESCIENDE por el indice n
    while (n != nullptr) {                  // no recorre la lista
        if (codigo == n->codigo) return n->dato; // cuando lo encuentra devuelve el Punto apuntado
        n = (codigo < n->codigo) ? n->izq : n->der; // en otro caso baja por la rama 
    }
    return nullptr;
}

static int altura(NodoIndice* n) {
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

int Sistema::alturaIndice() const { return altura(indice); }

static void borrarIndice(NodoIndice* n) {
    if (n == nullptr) return;
    borrarIndice(n->izq);
    borrarIndice(n->der);
    delete n;                      // NO se borra n->dato: es de la lista
}

void Sistema::liberarTodo() {
    Punto* a = lista;
    while (a != nullptr) {
        Punto* s = a->sig;         // guardar el siguiente ANTES de borrar
        delete a;
        a = s;
    }
    lista = nullptr;
    borrarIndice(indice);
    indice = nullptr;
}

void Sistema::ampliarCola() {
    int* nueva = new int[cap * 2];
    for (int i = 0; i < enCola; i++)
        nueva[i] = cola[(frente + i) % cap];        // en ORDEN DE SALIDA
    delete[] cola;
    cola = nueva;
    cap *= 2;
    frente = 0;
}

static int componentes(const vector<vector<int>>& g) {
    int V = (int)g.size();
    vector<bool> vis(V, false);
    int c = 0;
    for (int s = 0; s < V; s++) {
        if (vis[s]) continue;
        c++;
        vector<int> pila;                      // recorrido en PROFUNDIDAD
        pila.push_back(s); vis[s] = true;
        while (!pila.empty()) {
            int u = pila.back(); pila.pop_back();
            for (size_t t = 0; t < g[u].size(); t++)
                if (!vis[g[u][t]]) { vis[g[u][t]] = true; pila.push_back(g[u][t]); }
        }
    }
    return c;
}

vector<string> Sistema::viasCriticas() const {
    vector<string> out;
    int V = (int)red.size();
    for (size_t i = 0; i < aristas.size(); i++) {
        vector<vector<int>> g(V);
        for (size_t j = 0; j < aristas.size(); j++) {
            if (j == i) continue;
            g[aristas[j].first ].push_back(aristas[j].second);
            g[aristas[j].second].push_back(aristas[j].first);
        }
        if (componentes(g) > 1)
            out.push_back(to_string(aristas[i].first) + "-" + to_string(aristas[i].second));
    }
    return out;
}

// ============================================================
//   LO QUE USTED DEBE COMPLETAR
//   Son SEIS funciones: cinco aqui y una en analisis.py.
//   Estan acopladas: medir() usa buscar(), buscar() usa el indice que
//   construye registrar(), y mejorSeleccion() usa total().
//   Si registrar() queda mal, falla casi todo lo demas: empiece por ahi.
// ============================================================

// ---------------- PARTE A · memoria, lista e indice ----------------

Punto::~Punto() {
    // (6 puntos) El constructor pidio memoria con new[]. Devuelvala.
    // PENDIENTE
    delete[] mediciones;
}


bool Sistema::registrar(int codigo, const string& nombre, int cantidad) {
    // (24 puntos) ESTA ES LA FUNCION CENTRAL DEL PARCIAL.
    //
    // Debe hacer TRES cosas, y las tres tienen que quedar coherentes:
    //   1. Si el codigo ya existe, no registrar nada y devolver false.
    //      Tiene buscar() ya resuelta para averiguarlo.
    //   2. Crear el Punto e insertarlo en 'lista' manteniendola ORDENADA
    //      de forma ascendente por codigo. Contemple los tres casos:
    //      lista vacia, insercion antes de la cabeza, e insercion en el
    //      medio o al final.
    //   3. Insertar en 'indice' un NodoIndice con ese codigo que APUNTE
    //      al Punto que acabo de crear. El arbol es un BST por codigo.
    //      Puede escribir una funcion auxiliar libre en este archivo.
    //
    // El indice NO duplica la informacion: guarda un puntero al mismo
    // Punto que esta en la lista. Si inserta una copia, medir() escribira
    // en un sitio y total() leera de otro, y el sistema queda incoherente
    // sin dar un solo error de compilacion.
    //
    // PENDIENTE
    return false;
    // verificar si el codigo ya existe
    if (buscar(codigo) != nullptr) {
        return false; // cuando el codigo ya existe, no registra nada y devuelve false
    }
    // crear nuevo Punto 
    Punto* NuevoPunto = new Punto(codigo, nombre, cantidad); // el nuevo Punto tiene las mismas variables que el constructor de Punto
    // insertar NuevoPunto en la lista de forma ascendete por codigo
    if (lista == nullptr || lista->codigo > codigo) { // revisa que la lista esté vacia o que elc odigo nuevo sea menor que la cabeza de la lista
        NuevoPunto->sig = lista; // como cumpke una de las dos caracteristticas, el NuevoPunto apunta a la cabeza de la lista
        lista = NuevoPunto; // la cabeza de la lista ahora es el NuevoPunto
    } else {
        Punto* actual = lista; // la lista ya tiene al menos un dato y es menor al PuntoNuevo
        while (actual->sig != nullptr && actual->sig->codigo < codigo) { // ciclo mientras el siguiente no sea nulo y menor al actual
            actual = actual->sig;
        }
        NuevoPunto->sig = actual->sig;
        actual->sig = NuevoPunto;
    }
    // insertar en el indice NodoIndice
    NodoIndice* NuevoNodo = new NodoIndice(codigo, NuevoPunto); 
    // Hacer que el NodoIndice apunte al NuevoPunto
    if (indice == nullptr) { // revisa si si el indice está vacio
        indice = NuevoNodo; // el NuevoNodo es la cabeza del indice
    } else {
        NodoIndice* actual = indice; // el indice ya tiene al menos un dato
        while (true) {
            if (codigo < actual->codigo) { // si el codigo es menor que el actual, se mueve a la izquierda
                if (actual->izq == nullptr) { // si el izquierdo es nulo, se inserta el NuevoNodo
                    actual->izq = NuevoNodo;
                    break;
                }
                actual = actual->izq; // si no es nulo, se mueve a la izquierda
            } else { // si el codigo es mayor que el actual, se mueve a la derecha
                if (actual->der == nullptr) { // si el derecho es nulo, se inserta el NuevoNodo
                    actual->der = NuevoNodo;
                    break;
                }
                actual = actual->der; // si no es nulo, se mueve a la derecha
            }
        }

    }

}

// ---------------- PARTE B · consultas sobre el indice ----------------

vector<int> Sistema::enRango(int a, int b) const {
    // (14 puntos) Devuelve los codigos entre a y b, ambos incluidos,
    // en orden ASCENDENTE.
    //
    // No recorra todo el arbol para filtrar despues: PODE. Si el codigo
    // del nodo ya es menor o igual que a, no tiene sentido bajar por la
    // izquierda; si ya es mayor o igual que b, no tiene sentido bajar por
    // la derecha. La pregunta de la mesa es exactamente sobre esto.
    // PENDIENTE
    // devuelve el vector de codigo entre a y b en orden ascendente
    vector<int> codigos;
    // funcion PODE para recorrer las partes necesarias del arbol
    function<void(NodoIndice*)> enRangoAux = [&](NodoIndice* nodo) {
        if (nodo == nullptr) return; // si el nodo es nulo, retorna
        if (nodo->codigo > a) { // si el codigo del nodo es mayor que a, se mueve a la izquierda
            enRangoAux(nodo->izq);
        }
        if (nodo->codigo >= a && nodo->codigo <= b) { // si el codigo del nodo está entre a y b, se agrega al vector
            codigos.push_back(nodo->codigo);
        }
        if (nodo->codigo < b) { // si el codigo del nodo es menor que b, se mueve a la derecha
            enRangoAux(nodo->der);
        }
    };
    enRangoAux(indice);
    return codigos;
}

// ---------------- PARTE D · la red de puntos ----------------

vector<int> Sistema::rutaMinima(int origen, int destino) const {
    // (14 puntos) Devuelve la ruta con MENOS tramos entre los dos
    // vertices, como la secuencia de vertices desde 'origen' hasta
    // 'destino', ambos incluidos. Si no hay camino, devuelve un vector
    // vacio. Si origen == destino, devuelve {origen}.
    //
    // Use 'red', que ya esta construida. Recuerde que el recorrido que
    // garantiza el minimo numero de tramos es el de ANCHURA, y que para
    // reconstruir la ruta hace falta recordar de donde se llego a cada
    // vertice. Tiene viasCriticas() resuelta como ejemplo de recorrido
    // sobre la misma red.
    // PENDIENTE
    // busca la ruta con menos tramos mediante BFS
    vector<int> Sistema::RutaMinima(int origen, int destino) const { // se crea funcion RutaMinima con parametros origen y destine
        int V = red.size(); // almacena el tamaño de la ruta
        vector<int> ruta; // vector que almacena la ruta
        if (origen == destino) { // evalua que el origen sea igual al destino, al ser un unico tramo, devuelve el origen
            ruta.push_back(origen);
            return ruta;
        }
        vector<bool> visitado(red.size(), false); // vector que almacena vertices visitados
        vector<int> anterior(red.size(), -1); // vector almacena el vertice previo al actual
        queue<int> q; 
        q.push(origen); //agrega el origen a la cola
        visitado[origen] = true; //
        while (!q.empty()) { // ciclo mientra la cola no esté vacia
            int actual = q.front(); // almacena el vertice actual
            q.pop(); // elimina el evrtice de la cola
            for (int vecino : red[actual]) { // recorre los vecinos del vertie actual
                if (!visitado[vecino]) { 
                    visitado[vecino] = true; // marca el vecino como viistado
                    anterior[vecino] = actual; // almacena el vertice vecino como previo al actual
                    q.push(vecino); // agrega el vecino a la cola
                    if (vecino == destino) { // evalua que el vecino sea igual al destino
                        // reconstruir la ruta
                        int v = destino; // almacena el destino en v
                        while (v != -1) { // ciclo mientras v sea diferente de -1
                            ruta.push_back(v);
                            v = anterior[v];
                        }
                        reverse(ruta.begin(), ruta.end());
                        return ruta;
                    }
                }
            }
        }
        return ruta; // si no hay camino, devuelve un vector vacio
        }

    }

}

// ---------------- PARTE E · seleccion optima ----------------

vector<int> Sistema::mejorSeleccion(int capacidad) const {
    // (12 puntos) El vehiculo soporta 'capacidad' mediciones en total.
    // Cada punto ocupa 'nm' y aporta 'total()'. Cada punto se lleva o no
    // se lleva: no se parte ni se repite.
    //
    // Devuelva los CODIGOS de la seleccion de mayor aporte total que no
    // pase de la capacidad, en orden ascendente. Si hay empate en aporte,
    // la de MENOS puntos.
    //
    // Resuelvalo con recursion de tomar / no tomar, y pode la rama de
    // tomar cuando el punto ya no quepa.
    // PENDIENTE
    // definir una estructura para almacenar el codigo, nm y total de cada punto
    struct PuntoSeleccion { int codigo; int nm; int total; };
    // crear un vector de PuntoSeleccion a partir de la lista de puntos
    vector<PuntoSeleccion> puntos;
    for (Punto* a = lista; a != nullptr; a = a->sig) {
        puntos.push_back({a->codigo, a->nm, a->total()});
    }
    // definir una funcion recursiva para encontrar la mejor seleccion
    function<vector<int>(int, int, int)> mejorSeleccionAux = [&](int i, int capacidadRestante, int totalActual) {
        // caso base: si ya se revisaron todos los puntos, devuelve el vector vacio
        if (i == puntos.size()) return vector<int>(); 
        // no toma el punto actual
        vector<int> sinTomar = mejorSeleccionAux(i + 1, capacidadRestante, totalActual);
        vector<int> conTomar;
        if (puntos[i].nm <= capacidadRestante) {
            conTomar = mejorSeleccionAux(i + 1, capacidadRestante - puntos[i].nm, totalActual + puntos[i].total);
            conTomar.push_back(puntos[i].codigo);
        }
        // comparar las dos opciones y devolver la mejor
        if (conTomar.empty()) return sinTomar; // si no se puede tomar
        if (sinTomar.empty()) return conTomar; // si no se puede no tomar
        int totalSinTomar = 0;
        for (int codigo : sinTomar) {
            for (const auto& p : puntos) {
                if (p.codigo == codigo) {
                    totalSinTomar += p.total;
                    break;
                }
            }
        }       
        int totalConTomar = 0;
        for (int codigo : conTomar) {
            for (const auto& p : puntos) {
                if (p.codigo == codigo) {
                    totalConTomar += p.total;
                    break;
                }
            }
        }
        if (totalConTomar > totalSinTomar) return conTomar; // si el total de conTomar es mayor, devuelve conTomar
        if (totalConTomar < totalSinTomar) return sinTomar; // si el total de sinTomar es mayor, devuelve sinTomar
        // si son iguales, devuelve el que tenga menos puntos
        if (conTomar.size() < sinTomar.size()) return conTomar;
        if (conTomar.size() > sinTomar.size()) return sinTomar;
        // si son iguales, devuelve el que tenga los codigos en orden ascendente
        sort(conTomar.begin(), conTomar.end());
        sort(sinTomar.begin(), sinTomar.end());
        if (conTomar < sinTomar) return conTomar;
        if (conTomar > sinTomar) return sinTomar;
        // si son iguales, devuelve el vector vacio
        return {};
    };

    
    


    return {};
}
