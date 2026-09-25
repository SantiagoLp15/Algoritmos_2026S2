#Anotar una secuencia de pasos en un algoritmo
acciones = [
    {"nombre": "AAPL", "precio": 225.5},
    {"nombre": "AMZN", "precio": 185},
    {"nombre": "MU", "precio": 850},
    {"nombre": "NU", "precio": 8},
]

def selection_sort_stocks(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparaciones +=1
            if arr[j]['precio'] < arr[min_idx]['precio']:
                min_idx = j
                intercambios += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("La cantidad de comparaciones fue: ",comparaciones)
    print("La cantidad de intercambios fue: ",intercambios)
    return arr
resultado = selection_sort_stocks(acciones)
print(resultado)       