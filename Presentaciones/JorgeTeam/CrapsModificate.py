import random

saldo_jugador = 1000.00

def lanzar_dado():
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    return (dado1, dado2)

def mostrar_dado(dado):
    dado1, dado2 = dado
    print(f'Jugador lanzo {dado1} + {dado2} = {sum(dado)}')

def calcular_ganancia_apuesta(apuesta, resultado):
    if resultado == 'Gano':
        return apuesta
    else:
        return -apuesta

def mostrar_saldo(saldo):
    print(f'Saldo actual: ${saldo:.2f}')

while saldo_jugador > 0:
    apuesta = float(input("Ingrese la cantidad a apostar: "))
    if apuesta > saldo_jugador:
        print("No puedes apostar mas de tu saldo actual.")
        continue

    instruccion = input(
        "Para lanzar los dados, escriba 'lanzar'. Para retirarse, escriba 'retirar': ")

    if instruccion == 'lanzar':
        valor_dado = lanzar_dado()
        mostrar_dado(valor_dado)
        suma_de_dados = sum(valor_dado)

        if suma_de_dados in (7, 11):
            estatus_juego = 'Gano'
        elif suma_de_dados in (2, 3, 12):
            estatus_juego = 'Perdio'
        else:
            estatus_juego = 'Continua'
            mi_punto = suma_de_dados
            print('El punto es:', mi_punto)

        while estatus_juego == 'Continua':
            valor_dado = lanzar_dado()
            mostrar_dado(valor_dado)
            suma_de_dados = sum(valor_dado)

            if suma_de_dados == mi_punto:
                estatus_juego = 'Gano'
            elif suma_de_dados == 7:
                estatus_juego = 'Perdio'

        ganancia = calcular_ganancia_apuesta(apuesta, estatus_juego)
        saldo_jugador += ganancia
        mostrar_saldo(saldo_jugador)

        if saldo_jugador == 0:
            print("Saldo insuficiente. Juego terminado.")
            break

    elif instruccion == 'retirar':
        print("Juego terminado. Retiraste del juego.")
        break

    else:
        print("Instrucción inválida. Por favor, ingresa 'lanzar' o 'retirar'.")