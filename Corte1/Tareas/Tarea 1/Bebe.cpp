#include <iostream>

int main() {
    float peso=0;
    int mes=0;
    float dosis=0;
    std::cout<<"Ingrese el peso";
    std::cin>>peso;
    std::cout<<"Ingrese los meses";
    std::cin>>mes;
    dosis = (((peso+10)*8)/(mes*10));
    std::cout<<"La dosis apta para su bebé es de"<<dosis;
    return 0;
}