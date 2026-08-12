// Online C++ compiler to run C++ program online
#include <iostream>
int main() {
    double n1=0;
    double n2=0;
    double suma=0;
    double resta=0;
    double div=0;
    double mul=0;

    std::cout<<"Ingrese el primer numero";
    std::cin>>n1;
    std::cout<<"Ingrese el segundo numero";
    std::cin>>n2;
suma = n1+n2;
resta = n1-n2;
mul = n1*n2;
div = n1/n2;
std::cout<<"El resultado de la suma es"<<suma;
std::cout<<"El resultado de la resta es"<<resta;
std::cout<<"El resultado de la multiplicación es"<<mul;
std::cout<<"El resultado de la división es"<<div;



    return 0;
}