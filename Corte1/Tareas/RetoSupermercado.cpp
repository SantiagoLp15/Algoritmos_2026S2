
#include <iostream>
#include <ctime>
int main() {
    srand(time(NULL));
    int n1=(rand()%4)+1;
    int n2=0;
    int factura =0;
    std::cout<<"Ingrese el valor de su compra";
    std::cin>>n2;
    if (n2>50000){
        if (n1==1){
            factura = n2*0.9;
            std::cout<<"Obtuvo la bola roja, su descuento es del 10% y su total a pagar es "<<factura;
        }
        else if (n1==2){
            factura = n2*0.7;
            std::cout<<"Obtuvo la bola azul, su descuento es del 30% y su total a pagar es "<<factura;
        }
        else if (n1==3){
            factura = n2/2;
            std::cout<<"Obtuvo la bola amarilla, su descuento es del 50% y su total a pagar es "<<factura;
        }
        else {
            std::cout<<"Obtuvo la bola blanca, su compra es gratis "<<factura;
        }
    }
    else {
        std::cout<<"Su total a pagar es "<<n2;
    }


    return 0;
}