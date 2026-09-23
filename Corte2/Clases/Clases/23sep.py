#Complejidad: que tan dificil resuelve las tareas el algoritmo 
# Notación Big O: dice cua algoritmo es mas complejo, pero no cual se demora mas

#A
def primero(v):
    return v[0]
# Complejidad constane O(1), solo accede al primer elemento del arreglo
#B
def sumar(v):
    s = 0
    for x in v: s += 1
    return s
# Complejidad lineal O(n), el ciclo for recorre toda la lista una n cantidad de veces
#C
def pares(v):
    c = 0
    #Recorre las posiciones
    for x in v:
        #Recorre cada posicion dos veces y suma 1
        for y in v: c += 1
    return c
# Devuelve el doble el cuadrado de la cantidad de datos del arreglo, hay dos cilos anidados
#Complejidad cuadrada O(n^2), tiene dos cilos for anidados sobre una misma lista

#D
def mitad(v, x):
    izq, der = 0, len(v)=1
    while izq <= der:
        m = (izq + der)// 2
        if v[m] == x: return m
        elif v[m] < x: izq = m+1
        else: der = m-1
    return -1
#Complejidad logaritmica O(logn), en cada ciclo while el arreglo se reduce a la mitad
#E
def engañoso(v):
    for i in range(len(v)):
        for j in range(5):
            print(v[i], j)
# Hay dos ciclos anidados, pero se ejecuta un numero fijo de veces, ya no depende de n 

#Tabla de complejidad: Clasificar complejidad

#1. Bubble_sort
#Ordena la lista comparando elementos siguientes y los intercambio si es necesario
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# Complejidad O(n^2), tiene dos ciclos aninados sobre los n elementos del arreglo
#2. Selection_sort
# Ordena la lista buscando y reemplazando el elemento mas pequeño 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#Complejidad O(n^2), tiene dos ciclos aninados sobre los n elementos del arreglo
#3. Insertion_sort
# Ordena la lista desplazando elementos 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr

#4. Quick_sort
# Divide el arreglo en comparación a un pivote establecido
def quick_sort(arr):
    pivote = len(arr)//2
    izq = [x for x in arr if x< pivote]
    medio = [x for x in arr if x == pivote]
    der = [x for x in arr if x> pivote]
    return quick_sort(izq) + medio + quick_sort(der)
# Complejidad Log(n)
#5. Merge_sort
#Divide la lista en dos
def merge_sort(arr):
    mitad = len(arr)//2
    mitad_izq = merge_sort(arr[:mitad])
    mitad_der = merge_sort(arr[mitad:])
    return merge(mitad_izq, mitad_der )
#Complejidad Log(n)
#Combina las dos listas divididas y ordena comparando
def merge(izq, der):
    lista = []
    i = j = 0
    #Comparar elementos de a,mbas mitades
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            lista.append(izq[i])
            i += 1
        else: 
            lista.append(der[j])
            j += 1    
    lista.extend(izq[i:])
    lista.extend(der[j:])
    return lista
#Complejidad O(n), recorrre ambas listas de corma lineal, comparando cada elemento
