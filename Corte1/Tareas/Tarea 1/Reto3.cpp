#include <iostream>
#include <ctime>
int main() {
    srand(time(NULL));
    int n1=(rand()%2)+1;
    int n2=0;
    std::cout<<"Ingrese 1 para cara y 2 para sello";
    std::cin>>n2;
    if (n1==1){
        std::cout<<"Salió cara";
    }
    else {
        std::cout<<"Salió sello";
    }
    if(n1==n2){
        std::cout<<"Usted ganó";
        
    }
    else {
        std::cout<<"Usted perdió";
    }
   
    return 0;
}