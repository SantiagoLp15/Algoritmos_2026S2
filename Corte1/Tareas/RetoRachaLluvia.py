lluvia = [0, 1, 1, 0, 1, 1, 1, 0, 1]
racha = 0
mejor_racha = 0
for dia in lluvia:
    if dia == 1:
        racha += 1
        if racha > mejor_racha:
            mejor_racha = racha
    else:
        racha = 0

print("La racha más larga de días lluviosos es de", mejor_racha, "días.")