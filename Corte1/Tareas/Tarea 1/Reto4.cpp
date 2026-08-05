#include <iostream>
#include <ctime>
int main() {
    srand(time(NULL));
    int n1=(rand()%3)+1;
    int n2=0;
    std::cout<<"Ingrese 1 para piedra, 2 para papel y 3 para tijeras";
    std::cin>>n2;
    if(n1==1){
        std::cout<<"La maquina eligió piedra";
    }
    else if (n1==2){
        std::cout<<"La maquina eligió papel";
    }
    else {
        std::cout<<"La maquina eligió tijera";
    }
    if(n2==1){
        //El usuario eligió piedra
        if (n1==n2){
            std::cout<<"Usted eligió piedra, hubo empate";
        }
        else if (n1==2){
            //La mquina eligió papel
            std::cout<<"Usted eligió piedra y perdió";
        }
        else {
            std::cout<<"Usted eligió piedra y ganó";
        }
    }
    else if (n2 == 2) {
        //El usuario eligió papel
        if (n1==n2){
            std::cout<<"Usted eligió papel, hubo empate";
        }
        else if (n1==3){
            //La mquina eligió papel
            std::cout<<"Usted eligió papel y perdió";
        }
        else {
            std::cout<<"Usted eligió papel y ganó";
        }
    }
    else {
        //El usuario eligió tijera
        if (n1==n2){
            std::cout<<"Usted eligió tijera, hubo empate";
        }
        else if (n1==1){
            //La mquina eligió papel
            std::cout<<"Usted eligió tijera y perdió";
        }
        else {
            std::cout<<"Usted eligió tijera y ganó";
        }
    }
   
    return 0;
}