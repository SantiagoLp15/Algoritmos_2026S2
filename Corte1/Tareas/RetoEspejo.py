codigo = []
#Abrir un vector vacio para guardar el codigo 
while True:
#Repetir indefinidamente hasta que el usuario decida salir    
    linea = int(input("Ingrese el código (use '-1' para terminar): "))
    if linea == -1:
        break
    #Ahora el ciclo indefinido va a terminar cuando el usuario ingrese -1
    codigo.append(linea)
    #Con la linea 9, se va a ir guardando cada linea de codigo en el vector vacio que se creo al inicio 
izquierda = 0
#la avriable izqueirda representa el primer elemento del vector
derecha = len(codigo) - 1
#La variable derecha representa el ultimo elemento del vector
# len(codigo) es para identificar la cantidad de elementos que hay en el vector, y al restarle 1, se obtiene el indice del ultimo elemento
while izquierda <= derecha:
    #Mientras izquierda sea menor o igual a la variable derecha, se va a repetir el ciclo, se detiene luego de cruzarse
    if codigo[izquierda] != codigo[derecha]:
        print("El código no es un espejo.")
        break
    izquierda += 1
    derecha -= 1
else:
    print("El código es un espejo.")