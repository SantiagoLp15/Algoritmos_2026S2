# TEMPERATURAS DIARIAS 
# Para cada dia, calcular cuantos dias se debe esperar hasta que la temperatura sea mayor a la actual, si no hay, el resultado es cero.
# La salida espera es [1, 1, 4, 2, 1, 1, 0, 0]

dias = [73, 74, 75, 71, 69, 72, 76, 73] 

def cantidad_dias(dias):
    n = len(dias)
    posicion = [0]*n # Inicia en la primera posocion (0)
    pila = [] # La pila inicia vacia
    for i in range(n): # Se recorre la lista de temperaturas
        # Mediante un ciclo while, se recorre la pila, mientras no esté vacia y la temperatura actual (tope) sea menor a una temperatura proxima.
        while pila and dias[pila[-1]] < dias[i]:
            # Crear variable para ejecutrar pop()
            temp_inicial = pila.pop() # Se elimina el tope de la fila y se guarda en la avriable temp_inicial
            # Calcular la diferencia de la temperatura inicial y la proxima temperatura mayor.
            posicion[temp_inicial] = i - temp_inicial
            # Agregar la diferencia a la pila
        pila.append(i)
    return posicion
print(cantidad_dias(dias))


