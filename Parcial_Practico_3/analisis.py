# ============================================================
#  analisis.py · CASO F · PARTE F del parcial  (10 puntos)
#  AguaViva — Monitoreo de pozos rurales
#
#  VERIFICACION CRUZADA
#  Esta es la MISMA logica de Sistema::mejorSeleccion, escrita en el otro
#  lenguaje. El verificador compara los dos resultados: si no coinciden,
#  uno de los dos esta mal y el parcial no cierra.
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas.py
# ============================================================


def mejor_seleccion(codigos, pesos, valores, capacidad):
    """Devuelve la lista ORDENADA de codigos de la seleccion de mayor
       valor total que no pasa de 'capacidad'.

       codigos[i], pesos[i] y valores[i] describen el mismo punto.
       Cada punto se lleva o no se lleva. Si hay empate en valor, la
       seleccion con MENOS puntos.

       Debe dar exactamente el mismo resultado que la version en C++.

       PENDIENTE: implementar con recursion de tomar / no tomar y poda."""
    pass
def mejor_seleccion(codigos, pesos, valores, capacidad):
    n = len(codigos)
    mejor_valor = 0
    mejor_seleccion = []
    def backtrack(i, seleccion_actual, peso_actual, valor_actual):
        nonlocal mejor_valor, mejor_seleccion
        if peso_actual > capacidad:
            return
        if valor_actual > mejor_valor or (valor_actual == mejor_valor and len(seleccion_actual) < len(mejor_seleccion)):
            mejor_valor = valor_actual
            mejor_seleccion = seleccion_actual[:]
        if i >= n:
            return
        # Tomar el punto actual
        backtrack(i + 1, seleccion_actual + [codigos[i]], peso_actual + pesos[i], valor_actual + valores[i])
        # No tomar el punto actual
        backtrack(i + 1, seleccion_actual, peso_actual, valor_actual)
    backtrack(0, [], 0, 0)
    return sorted(mejor_seleccion)
