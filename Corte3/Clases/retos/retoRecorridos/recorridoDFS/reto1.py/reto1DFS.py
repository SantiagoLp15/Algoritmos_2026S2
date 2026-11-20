# El detector de islas · Obligatorio Sobre la red de su proyecto, escriba un informe automático que diga cuántas componentes hay, 
# cuáles vértices tiene cada una, y cuál es la más grande. Después elimine dos aristas a propósito y vuelva a correrlo.

#-------------Reto 2--------------------

# El plan de estudios imposible · Obligatorio Construya un grafo DIRIGIDO de prerrequisitos con al menos seis asignaturas
# e introduzca a propósito un ciclo. Escriba un detector de ciclos para grafos dirigidos y haga que informe cuáles asignaturas forman
# el ciclo.
pensum = {
    # Donde las llaves son las materias que desbloquea cada clase
    'Cálculo I':  ['Cálculo II', 'Macro I', 'Micro I'],
    'Cálculo II': ['Macro II'],
    'Macro I':    ['Macro II'],
    'Macro II':   ['Cálculo I'],  # Ahi está el ciclo
    'Micro I':    ['Micro II'],
    'Micro II':   []
}
def detectar_ciclo_pensum(grafo):
    # Cada asignatura inicia en 0 ya que al inciio no se ha visto ninguna materia
    estado = {materia: 0 for materia in grafo}
    # Lista vacia que alamcena el recorrido 
    ruta_actual = []

    def dfs(materia): # funciona para cada asignatura especifica
        estado[materia] = 1 # Se exploran los psobles caminos que tiene esa materia
        ruta_actual.append(materia)

        # Se pasa a revisar todas la materias que dependen de esa
        for siguiente in grafo[materia]:
            if estado[siguiente] == 1:
                # Una materia es 1 cuando ya está en proceso, para este caso, que sea 1 involucra que hay un ciclo
                inicio_ciclo = ruta_actual.index(siguiente)
                ciclo_exacto = ruta_actual[inicio_ciclo:] + [siguiente]
                print("Ciclo detectado, el plan de estudios es imposible de llevar a cabo")
                print("   " + " -> ".join(ciclo_exacto))
                return True
            # Cuando al materia es 0 es porque aun no se ha recorrido
            elif estado[siguiente] == 0: 
                # repite la funcion dfs ya que es un camino nuevo
                if dfs (siguiente):
                    return True
        estado[materia] = 2 # Ya terminó la linea de esa materia
        ruta_actual.pop() # La materia sale de la ruta actual
        return False
    # Continua la búsqueda desde cada materia que siga sin visitar
    for materia in grafo:
        if estado[materia] == 0: # evalua que no se haya visitado
            if dfs(materia): # llama la funcion
                return
    print(" Plan de estudios valido")
detectar_ciclo_pensum(pensum)