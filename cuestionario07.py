# asuma que la variable descripcion es una variable global
# correctamente definida como una tupla de esta forma:

import random
descripcion = 'Piedra', 'Papel', 'Tijera'

# leer jugada del humano...
humano = int(input('Ingrese 1 - Piedra, 2 - Papel o 3 - Tijera: '))
print('Usted eligio:', descripcion[humano - 1])

# generar jugada del computador...
computadora = random.randint(0, 2)
print('La computadora eligio:', descripcion[computadora ])

# determinar si hubo un ganador...
if humano != computadora:
    if (humano == 1 and computadora == 3) \
            or (humano == 3 and computadora == 2) \
            or (humano == 2 and computadora == 1):
        ganador = 1
        print('gano humando')
    else:
        ganador = -1
        print('gano maquina')
else:
    ganador = 0
    print('empate')
