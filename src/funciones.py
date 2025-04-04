def calcular_puntos(kills, asistencias, muertes):
    if muertes == True:
        muertes = 1
    else:
        muertes = 0
    
    puntos = kills * 3 + asistencias * 1 - muertes * 1

    return puntos 

def inicializar_ronda(cada_ronda):
    for jugador in cada_ronda:
        cada_ronda[jugador]['kills'] = 0
        cada_ronda[jugador]['assists'] = 0    
        cada_ronda[jugador]['deaths'] = 0
        cada_ronda[jugador]['puntos'] = 0
    