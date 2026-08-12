
#include <iostream>
#include <ctime>
int main() {
    srand(time(NULL));
    int n1=(rand()%6)+1;
    int n2=(rand()%6)+1;
    std::cout<<"El resultado de los numeros fue "<<n1<<" y "<< n2;
    if (n1==1 and n2==1){
        std::cout<<"El resultado de los numeros fue par de unos, usted ganó";
    }
    if (n1+n2==3){
        std::cout<<"La suma de los numeros es tres, usted ganó";
    }
    if (n1+n2==11){
        std::cout<<"La suma de los numeros es 11, usted ganó";
    }
    if (n1+n2==2){
        std::cout<<"La suma de los numeros es dos, usted ganó";
    }
    if (n1+n2==12){
        std::cout<<"La suma de los numeros es 12, usted ganó";
    }
    if (n1+n2==7){
        std::cout<<"La suma de los numeros es 7, usted ganó";
    }

    return 0;
}