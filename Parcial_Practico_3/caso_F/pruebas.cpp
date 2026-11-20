// NO MODIFIQUE ESTE ARCHIVO. Alterarlo se considera fraude academico
// segun la seccion 13 de la guia de asignatura.
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include "sistema.h"
using namespace std;

// ---- datos del caso F ----
static int          COD[8]  = {142, 812, 663, 733, 325, 933, 642, 807};
static const char*  NOM[8]  = {"ESTACION", "POZO1", "POZO2", "POZO3", "TANQUE", "BOMBEO", "FILTRO", "VEREDA"};
static int          NME[8]  = {4, 4, 3, 6, 6, 6, 4, 6};
static int          MED[][3] = {{0, 0, 38}, {0, 1, 40}, {0, 2, 6}, {0, 3, 6}, {1, 0, 10}, {1, 1, 25}, {1, 2, 34}, {1, 3, 15}, {2, 0, 27}, {2, 1, 33}, {2, 2, 2}, {3, 0, 10}, {3, 1, 31}, {3, 2, 4}, {3, 3, 39}, {3, 4, 2}, {3, 5, 15}, {4, 0, 9}, {4, 1, 12}, {4, 2, 26}, {4, 3, 34}, {4, 4, 17}, {4, 5, 37}, {5, 0, 29}, {5, 1, 16}, {5, 2, 27}, {5, 3, 20}, {5, 4, 6}, {5, 5, 29}, {6, 0, 28}, {6, 1, 17}, {6, 2, 33}, {6, 3, 34}, {7, 0, 24}, {7, 1, 31}, {7, 2, 15}, {7, 3, 25}, {7, 4, 5}, {7, 5, 36}};
static const int    NMED = 39;
static vector<pair<int,int>> VIAS = {{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 4}, {2, 5}, {3, 6}, {4, 5}, {6, 7}};
static const int    VERT = 8;
static const int    CAPV = 16;
static const int    COLA = 4;

static void cargar(Sistema& S) {
    for (int i = 0; i < 8; i++) S.registrar(COD[i], NOM[i], NME[i]);
    for (int i = 0; i < NMED; i++) S.medir(COD[MED[i][0]], MED[i][1], MED[i][2]);
}

static int fallas = 0;
static string lista2s(const vector<int>& v) {
    string r; for (size_t i=0;i<v.size();i++) { if(i) r+=","; r+=to_string(v[i]); } return r;
}
static void chkS(const string& n, const string& o, const string& e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo \"" << o << "\"";
    if (!ok) cout << "\n          esperaba \"" << e << "\"";
    cout << endl; if (!ok) fallas++;
}
static void chkI(const string& n, int o, int e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo " << o;
    if (!ok) cout << "  (esperaba " << e << ")";
    cout << endl; if (!ok) fallas++;
}

int main() {
    cout << "PARTE C++ · sistema integrado · caso F" << endl;
    cout << "----------------------------------------------------------" << endl;
    Sistema S(COLA, VIAS, VERT);
    cargar(S);

    cout << " A · memoria, lista e indice" << endl;
    chkS("la lista queda ordenada por codigo", S.codigos(), "142 325 642 663 733 807 812 933");
    chkI("cuantos puntos registrados", S.cuantos(), 8);
    chkI("altura del indice", S.alturaIndice(), 4);
    chkI("un codigo repetido no se registra", S.registrar(COD[0], "OTRO", 3) ? 1 : 0, 0);
    chkI("el repetido no altero la cantidad", S.cuantos(), 8);
    chkI("suma de todas las mediciones", S.sumaTotales(), 847);

    cout << " B · consultas sobre el indice" << endl;
    Punto* p = S.buscar(COD[3]);
    chkS("buscar devuelve el punto correcto", p ? p->nombre : string("NULO"), "POZO3");
    chkI("el indice apunta al MISMO punto de la lista", p ? p->total() : -1, 101);
    chkI("buscar un codigo ausente devuelve nulo", S.buscar(1) == nullptr ? 1 : 0, 1);
    chkS("rango amplio: todos en orden", lista2s(S.enRango(0, 1000)), "142,325,642,663,733,807,812,933");
    chkS("rango acotado [642, 807]", lista2s(S.enRango(642, 807)), "642,663,733,807");
    chkS("rango sin resultados", lista2s(S.enRango(1, 2)), "");

    cout << " C · cola circular" << endl;
    for (int i = 0; i < COLA; i++) S.encolar(COD[i]);
    chkI("encolar en cola llena devuelve false", S.encolar(COD[5]) ? 1 : 0, 0);
    chkS("cola llena", S.enEspera(), "142 812 663 733");
    int x;
    S.siguiente(x); chkI("siguiente devuelve el frente", x, 142);
    S.siguiente(x);
    S.encolar(COD[6]); S.encolar(COD[7]);
    chkS("los datos dieron la vuelta", S.enEspera(), "663 733 642 807");
    chkI("capacidad antes de ampliar", S.cap, 4);
    S.ampliarCola();
    chkI("capacidad duplicada", S.cap, 8);
    chkI("frente reubicado en 0", S.frente, 0);
    chkS("orden conservado tras ampliar", S.enEspera(), "663 733 642 807");
    S.encolar(COD[0]);
    chkS("sigue funcionando tras ampliar", S.enEspera(), "663 733 642 807 142");

    cout << " D · la red de puntos" << endl;
    chkS("ruta minima 0 -> 7", lista2s(S.rutaMinima(0, 7)), "0,3,6,7");
    chkS("ruta minima 0 -> 5", lista2s(S.rutaMinima(0, 5)), "0,2,5");
    chkS("ruta de un vertice a si mismo", lista2s(S.rutaMinima(3, 3)), "3");
    vector<string> vc = S.viasCriticas();
    string sc; for (size_t i=0;i<vc.size();i++) { if(i) sc+=","; sc+=vc[i]; }
    chkS("vias criticas", sc, "0-3,3-6,6-7");

    cout << " E · seleccion optima" << endl;
    vector<int> sel = S.mejorSeleccion(CAPV);
    chkS("mejor seleccion con capacidad 16", lista2s(sel), "325,642,807");
    int aporte = 0, peso = 0;
    for (size_t i=0;i<sel.size();i++) { Punto* q=S.buscar(sel[i]); aporte+=q->total(); peso+=q->nm; }
    chkI("aporte total de la seleccion", aporte, 383);
    chkI("la seleccion cabe en la capacidad", peso <= CAPV ? 1 : 0, 1);
    chkS("seleccion con capacidad 0", lista2s(S.mejorSeleccion(0)), "");

    cout << "----------------------------------------------------------" << endl;
    if (fallas == 0) {
        // Se entrega a la PARTE F lo necesario para la verificacion cruzada.
        ofstream f("cruce.txt");
        f << "cuantos=" << S.cuantos() << "\n";
        f << "suma="    << S.sumaTotales() << "\n";
        f << "altura="  << S.alturaIndice() << "\n";
        f << "capacidad=" << CAPV << "\n";
        string cods, pes, vals;
        for (Punto* a = S.lista; a != nullptr; a = a->sig) {
            if (!cods.empty()) { cods += ","; pes += ","; vals += ","; }
            cods += to_string(a->codigo);
            pes  += to_string(a->nm);
            vals += to_string(a->total());
        }
        f << "codigos="  << cods << "\n";
        f << "pesos="    << pes  << "\n";
        f << "valores="  << vals << "\n";
        f << "seleccion=" << lista2s(sel) << "\n";
        f << "aporte="   << aporte << "\n";
        f.close();
        cout << "  PARTE C++ COMPLETA. Ahora ejecute la PARTE F:  python3 pruebas.py" << endl;
    } else {
        remove("cruce.txt");
        cout << "  PARTE C++ INCOMPLETA (" << fallas << " falla(s))." << endl;
        cout << "  Corrija y vuelva a ejecutar. El codigo de cierre sale al final," << endl;
        cout << "  cuando las dos partes del sistema funcionen." << endl;
    }
    return 0;
}
