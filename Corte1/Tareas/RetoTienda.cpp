#include <iostream>
using namespace std;

int main() {

    int productos, cantidad;
    double precio, subtotal;
    double total = 0;
    double descuento;
    double total_pagar;
    string nombre;

    cout << "Cuantos productos va a comprar? ";
    cin >> productos;

    for (int i = 1; i <= productos; i++) {

        cout << "\nProducto " << i << endl;

        cout << "Nombre del producto: ";
        cin >> nombre;

        cout << "Precio unitario: ";
        cin >> precio;

        cout << "Cantidad comprada: ";
        cin >> cantidad;

        subtotal = precio * cantidad;

        total = total + subtotal;

        cout << "Subtotal de " << nombre << ": " << subtotal << endl;
    }

    if (total > 300000) {

        descuento = total * 0.10;

    } else if (total >= 150000) {

        descuento = total * 0.05;

    } else {

        descuento = 0;
    }

    total_pagar = total - descuento;

    cout << "\n-----------------------------" << endl;
    cout << "Total antes del descuento: " << total << endl;
    cout << "Descuento aplicado: " << descuento << endl;
    cout << "Total a pagar: " << total_pagar << endl;

    return 0;
}