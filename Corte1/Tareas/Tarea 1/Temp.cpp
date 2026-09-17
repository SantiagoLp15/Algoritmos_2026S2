#include <iostream>

int main() {
    float n1=0;
    float n2=0;
    std::cout<<"Ingrese la temperatura en centigrados";
    std::cin>>n1;
    n2 = (n1-32)/1.8;
    std::cout<<"Su temperatura es"<<n2;
   

    return 0;
}