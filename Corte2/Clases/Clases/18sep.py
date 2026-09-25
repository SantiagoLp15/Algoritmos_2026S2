# Ordenamientos: organizar una coleccion con elementos que queden en secuencia según un criterio
#
# ORDENAMIENTO BASICO: 
# 
# 1. Bubble sort:Comparación entre vecinos y posible intercambio de posiciones
# 2. Selection sort: Tomo el mas pequeño y lo ubico en la primera posicion
# 3. Insertion sort: El elemento dos se ubica en el segundo puesto

# comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hast que nadie mas se mueva bubble sort

#n = [64, 25, 12, 22, 11, 90, 45, 33]
n = [1, 2, 3, 4, 5, 6, 7, 8]


def bubble_sort(arr):
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True
        if not swapped:
            break
    print("La cantidad de comparaciones fue: ",comparaciones)
    print("La cantidad de intercambios fue: ",intercambios)
    return arr
#buscar el más pequeño y ponerlo al 
# principio selection sort

def selection_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones +=1
            if arr[j] < arr[min_idx]:
                min_idx = j
                intercambios +=1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("La cantidad de comparaciones fue: ",comparaciones)
    print("La cantidad de intercambios fue: ",intercambios)
    return arr
# tomo el segubndo y lo inserto donde va 
# respecto al primero insertion sort

def insertion_sort(arr):
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                intercambios += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    print("La cantidad de comparaciones fue: ",comparaciones)
    print("La cantidad de intercambios fue: ",intercambios)
    return arr
# Cada función recibe su propia copia de la lista original para que no afecte el resultado de las demás.
print("--- Bubble sort ---")
print(bubble_sort(n.copy()))

print("\n--- Selection sort ---")
print(selection_sort(n.copy()))

print("\n--- Insertion sort ---")
print(insertion_sort(n.copy()))

# --- MARGE Y QUICK ---

def particion(arr, low, high, contadores):
    pivote = arr[high]  # Elegimos el último elemento de la lista como pivote
    i = low - 1         # Frontera de elementos menores al pivote
    
    for j in range(low, high):
        contadores["comparaciones"] += 1
        # Si j es menor al pivote, se hace el ntercambio 
        if arr[j] < pivote:
            i += 1
            # Intercambio del elemento pequeño a la izquierda
            arr[i], arr[j] = arr[j], arr[i]
            contadores["intercambios"] += 1
            
    # Colocamos el pivote en su posición correcta final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    contadores["intercambios"] += 1
    
    return i + 1  # Retornamos la posición donde quedó el pivote


# --- Quicksort ---
def quicksort_rec(arr, low, high, contadores):
    if low < high:
        # pi es el índice donde el pivote ya quedó bien ubicado
        pi = particion(arr, low, high, contadores)  
        # Ordenamos los elementos antes y después de la partición
        quicksort_rec(arr, low, pi - 1, contadores)
        quicksort_rec(arr, pi + 1, high, contadores)


# --- Función Wrapper para llamar de forma sencilla ---
def quicksort(arr):
    contadores = {"comparaciones": 0, "intercambios": 0}
    quicksort_rec(arr, 0, len(arr) - 1, contadores)
    
    print("La cantidad de comparaciones fue:", contadores["comparaciones"])
    print("La cantidad de intercambios fue:", contadores["intercambios"])
    return arr


# --- Prueba de Ejecución ---
datos = [64, 25, 12, 22, 11, 90, 45, 33]
print("Lista ordenada:", quicksort(datos.copy()))