matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0
for i in range(len(matriz)):
    suma_diagonal_principal += matriz[i][i]
    suma_diagonal_secundaria += matriz[i][len(matriz) - 1 - i]  
    
print(f"La suma de la diagonal principal es: {suma_diagonal_principal}")
print(f"La suma de la diagonal secundaria es: {suma_diagonal_secundaria}")

if suma_diagonal_principal == suma_diagonal_secundaria:
    print("Las sumas de las diagonales son iguales, el codigo es correcto.")