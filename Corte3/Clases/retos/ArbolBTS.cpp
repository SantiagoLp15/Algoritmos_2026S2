#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Nodo {
    int clave; string nombre;
    Nodo *izq, *der;
    Nodo(int c, string n = "") : clave(c), nombre(n), izq(nullptr), der(nullptr) {}
};
// Se crea la funcion para insertar
Nodo* insertar(Nodo* n, int clave, string nombre="") {
    if(n==nullptr) return new Nodo(clave, nombre);
    if (clave < n->clave) n->izq = insertar(n->izq, clave, nombre);
    else if (clave > n->clave) n->der = insertar(n->der, clave, nombre);
    return n;
}
// Se crea la funcion para buscar
Nodo* buscar(Nodo* n, int clave, vector<string>* pasos = nullptr) {
    if (pasos != nullptr) {
        if (n == nullptr) pasos->push_back("vacio"); 
        else pasos->push_back(to_string(n->clave));
    }
    if (n == nullptr || n->clave == clave) return n;
    if (clave < n->clave) return buscar(n->izq, clave, pasos);
    else return buscar(n->der, clave, pasos);
}
// Se crea la funcion para buscar el minimo
Nodo* minimo(Nodo* n) {
    while (n->izq != nullptr) n = n->izq;
    return n;
}
// Se crea la funcion para buscar el maximo
Nodo* maximo(Nodo* n) {
    while (n->der != nullptr) n = n->der;
    return n;
}
// Se crea la funcion para eliminar
Nodo* eliminar(Nodo* n, int clave) {
    if (n == nullptr) return nullptr;
    if (clave < n->clave) n->izq = eliminar(n->izq, clave);
    else if (clave > n->clave) n->der = eliminar(n->der, clave);
    else {  // Busca el el nodo a eliminar
        if (n->izq == nullptr) {          // 0 hijos o solo hijo derecho
            Nodo* hijo = n->der;
            delete n;                     // Libera la memoria
            return hijo;
        }
        if (n->der == nullptr) {          // 0 hijos o solo hijo izquierdo
            Nodo* hijo = n->izq;
            delete n;
            return hijo;
        }
        // En caso de dos hijos, se copia el minimo del lado derecho y se borra
        Nodo* suc = minimo(n->der);
        n->clave = suc->clave;
        n->nombre = suc->nombre;
        n->der = eliminar(n->der, suc->clave);
    }
    return n;
}
// ordena la lista
void inorden(Nodo* n, vector<int>& s) {
    if (n == nullptr) return;
    inorden(n->izq, s);
    s.push_back(n->clave);
    inorden(n->der, s);
}
// calcula la altura del nodo
int altura(Nodo* n) {
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

// Devuelve cuantos hijos tiene el nodo, da -1 si no existe
int hijos(Nodo* n, int clave) {
    n = buscar(n, clave);
    if (n == nullptr) return -1;
    int cuenta = 0;
    if (n->izq != nullptr) cuenta++;
    if (n->der != nullptr) cuenta++;
    return cuenta;
}

// Imprime la lista ya ordenada
void verLista(string titulo, const vector<int>& s) {
    if (titulo != "") cout << titulo << " ";
    cout << "[";
    for (size_t i = 0; i < s.size(); i++) {
        cout << s[i];
        if (i + 1 < s.size()) cout << ", ";
    }
    cout << "]" << endl;
}

// libera el arbol
void liberar(Nodo* n) {
    if (n == nullptr) return;
    liberar(n->izq);
    liberar(n->der);
    delete n;
}

int main() {
    Nodo* raiz = nullptr;
    for (int c : {50, 30, 70, 20, 40, 60, 80, 35}) raiz = insertar(raiz, c);
    vector<int> s; inorden(raiz, s);
    verLista("Inorden (queda ordenado):", s);
    cout << "minimo = " << minimo(raiz)->clave << "  maximo = " << maximo(raiz)->clave
         << "  altura = " << altura(raiz) << endl;

    for (int objetivo : {40, 65}) {
        vector<string> p; Nodo* r = buscar(raiz, objetivo, &p);
        cout << "buscar(" << objetivo << "): camino ";
        for (size_t i = 0; i < p.size(); i++) { cout << p[i]; if (i + 1 < p.size()) cout << " ->"; }
        cout << "  =>" << (r ? "ENCONTRADO" : "NO ESTA")
             << " (" << p.size() << " comparaciones)" << endl;
    }
    const char* NOMBRE[] = {"caso 1: hoja, 0 hijos", "caso 2: un hijo", "caso 3: dos hijos"};
    for (int clave : {20, 30, 50}) {
        int k = hijos(raiz, clave);                 // se mide, no se supone
        raiz = eliminar(raiz, clave);
        s.clear(); inorden(raiz, s);
        cout << "eliminar(" << clave << ") [" << NOMBRE[k] << "] -> ";
        verLista("", s);
    }
    Nodo* deg = nullptr;
    for (int c : {10, 20, 30, 40, 50, 60, 70, 80}) deg = insertar(deg, c);
    cout << "\nBTS con datos ordenados: altura = " << altura(deg) << " con 8 nodos (una lista enlazada)" << endl;
    cout << "BTS con datos mezclados: altura = " << altura(raiz) << " con 8 nodos (log2(8) = 3)" << endl;

    liberar(raiz); liberar(deg);
    return 0;
}