computador = [2, 5, 3, 8, 6]
vdb = [1, 4, 7, 9, 10]
sala = [11, 12, 13, 14, 15]
for i in range(5):
    total_lunes = computador[0] + vdb[0] + sala[0]
    print("El total de lunes es de ", total_lunes)
    total_martes = computador[1] + vdb[1] + sala[1]
    print("El total de martes es de ", total_martes)
    total_miercoles = computador[2] + vdb[2] + sala[2]
    print("El total de miércoles es de ", total_miercoles)
    total_jueves = computador[3] + vdb[3] + sala[3]
    print("El total de jueves es de ", total_jueves)
    total_viernes = computador[4] + vdb[4] + sala[4]
    print("El total de viernes es de ", total_viernes)
    carga = [total_lunes, total_martes, total_miercoles, total_jueves, total_viernes]
    for x in range(5):
        if carga[x] == max(carga):
            match x:
                case 0:
                    print("El día con mayor carga de trabajo es el lunes")
                case 1:
                    print("El día con mayor carga de trabajo es el martes")
                case 2:
                    print("El día con mayor carga de trabajo es el miércoles")
                case 3:
                    print("El día con mayor carga de trabajo es el jueves")
                case 4:
                    print("El día con mayor carga de trabajo es el viernes")
                case _:
                    print("Error")
            


            

