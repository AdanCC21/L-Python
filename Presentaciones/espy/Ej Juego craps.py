"""
    Gonzalez Cesena Adan
    941
"""


import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import statistics as st

def throwDice():
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    return (d1, d2) 

def showDice(dado):
    dado1, dado2 = dado
    print(f'Jugador lanzó {dado1} + {dado2} = {sum(dado)}')

# Listas para contar victorias y derrotas
win = [0] * 14
lose = [0] * 14

duracionjuegos = {}

if len(sys.argv) < 2:
    throw = int(input("Ingrese el número de juegos a simular: "))
else:
    throw = int(sys.argv[1])

for _ in range(throw):
    juegoNumero = 1
    
    valordado = showDice()  # Primer tiro
    sumdados = sum(valordado)

    if sumdados in (7, 11):  # Gano
        estatusjuego = 'Ganó'
    elif sumdados in (2, 3, 12):  # Perdio
        estatusjuego = 'Perdió'
    else:  # Recuerda el punto
        estatusjuego = 'Continua'
        punto = sumdados

    # Continúa lanzando hasta que el jugador gana o pierde
    while estatusjuego == 'Continua':
        valordado = throwDice()
        sumdados = sum(valordado)
    
        if sumdados == punto:  # Ganó por los puntos
            estatusjuego = 'Ganó'
            duracion = juegoNumero
            if duracion in duracionjuegos:
                duracionjuegos[duracion] += 1
            else:
                duracionjuegos[duracion] = 1
            break
        elif sumdados == 7:  # Perdió lanzando 7
            estatusjuego = 'Perdió'
            break

        juegoNumero += 1

    if estatusjuego == 'Ganó':
        if juegoNumero >= 13:
            win[13] += 1
        else:
            win[juegoNumero] += 1
    elif estatusjuego == 'Perdió':
        if juegoNumero >= 13:
            lose[13] += 1
        else:
            lose[juegoNumero] += 1
   

# Probabilidad de ganar general
twin = sum(win)
probwin = twin / throw

# Obtener probabilidades de ganar en una lista
probganar = [win[v] / twin for v in range(len(win))]
pbredondeado = [round(prob, 4) for prob in probganar]

# MEDIA
totaljuego = sum(duracionjuegos.values())
media = st.mean(duracionjuegos)

# MEDIANA
sorted_data = sorted(duracionjuegos)
mediana = st.median(sorted_data)

# MODA
moda = st.mode(duracionjuegos)

# Mostrar en la terminal los datos
print(f'Victorias: {win}')
print(f'Derrotas: {lose}')
print(f'La probabilidad de ganar es: {probwin}')
print(f'La media de duración de los juegos: {media:.4f}')
print(f'La mediana de duración de los juegos: {mediana:.4f}')
print(f'Moda de duración de los juegos: {moda} veces')
print(f'Las probabilidades de ganar es: {pbredondeado}')


# Grafica
y = np.arange(14)
x1 = win
x2 = lose

plt.barh(y, x1, color='b', label='Victorias')
plt.barh(y, x2, color='r', label='Derrotas', left=x1)
plt.ylabel('Jugadas')
plt.xlabel('Cantidad de veces')
plt.title('Victorias y Derrotas')
plt.legend()
plt.show()
