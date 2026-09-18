# Ordenamientos: organizar una coleccion con elementos que queden en secuencia según un criterio
#
# ORDENAMIENTO BASICO: 
# 
# 1. Bubble sort:Comparación entre vecinos y posible intercambio de posiciones
# 2. Selection sort: Tomo el mas pequeño y lo ubico en la primera posicion
# 3. Insertion sort: El elemento dos se ubica en el segundo puesto

# comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hast que nadie mas se mueva bubble sort

n = [64, 25, 12, 22, 11, 90, 45, 33]

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

            