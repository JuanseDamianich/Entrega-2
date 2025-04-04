from src.funciones import calcular_puntos, inicializar_ronda


rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]

estadisticas = {
'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0}
}

cada_ronda = {
'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0},
'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos': 0}
}




# Recorrer las rondas
for i, ronda in enumerate(rounds, start = 1):
    print(f"Ronda {i}:")
    
    max = 0
    mvp = None

    inicializar_ronda(cada_ronda)

    # Recorrer cada jugador en la ronda
    for jugador, stats in ronda.items():

        kills = stats['kills']
        asistencias = stats['assists']
        muertes = stats['deaths']
        puntos = calcular_puntos(kills, asistencias, muertes)

        # determinar el MVP
        if puntos > max: 
            max = puntos
            mvp = jugador

        # asignar puntos a la ronda particular 
        cada_ronda[jugador]['kills'] = kills
        cada_ronda[jugador]['assists'] = asistencias
        cada_ronda[jugador]['deaths'] = muertes
        cada_ronda[jugador]['puntos'] = puntos

        # asignar los puntos de la ronda a las estadisticas totales
        estadisticas[jugador]['kills'] += kills
        estadisticas[jugador]['assists'] += asistencias
        estadisticas[jugador]['deaths'] += muertes
        estadisticas[jugador]['puntos'] += puntos
    
    # sumar el MVP a quien lo gano en esta ronda
    estadisticas[mvp]['MVP'] += 1
    
    print('El MVP de la ronda fue: ', mvp)

    jugadores_ordenados = sorted(cada_ronda.items(), key = lambda x: x[1]['puntos'], reverse = True)
    # esta linea devuelve los datos del diccionario 'estadisticas' ordenados de forma descendente por la 
    # llave elegida 'puntos' 
    
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<12} {'Muertes':<7} {'MVP':<4} {'Puntos Totales':<15}")
    # imprime el encabezado del cuadro de puntos. El ':<' orienta el texto a la izquierda y el '10'
    # son la cantidad de caracteres del espacio de la columna(si lo escrito en la columna no lo alcanza
    # se rellena con espacios)

    for jugador, stats in jugadores_ordenados:
        print(f"{jugador:<10} {stats['kills']:<6} {stats['assists']:<12} {stats['deaths']:<7} {stats['MVP']:<4} {stats['puntos']:<15}")
        # lo mismo que antes pero de las estadisticas de los jugadores 

    print('\n')

print('\n')
print('Ranking Final:')

ranking_ordenado = sorted(estadisticas.items(), key = lambda x: x[1]['puntos'], reverse = True)

for jugador, stats in ranking_ordenado:
        print(f"{jugador:<10} {stats['kills']:<6} {stats['assists']:<12} {stats['deaths']:<7} {stats['MVP']:<4} {stats['puntos']:<15}")
