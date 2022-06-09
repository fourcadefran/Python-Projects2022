# Constantes
import random
carta_as = 1
num_carta = carta_as, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'
acum_pozos = 0
puede_jugar = True

#porcentaje de victorias jugador
porc_vict_jug = total_manos = cont_vict_jug = 0

#Racha de victorias crupier
racha_vict_crup = max_racha_crup = 0
vict_ant_crup = False

#Contar las manos con BJ natural
cont_bj_natural = 0
salio_bjn = salio_bjn_crup = False

#Monto maximo en el pozo
monto_max_pozo = 0

#Monto promedio en el pozo
pozo_acum = prom_pozo_jug = 0

#perdida mas alta del jugador
perd_jug = 0
perdida_max = 0

#Funciones
def pedir_carta():
    carta = random.choice(num_carta)
    if carta == 'J' or carta == 'Q' or carta == 'K':
        carta = 10
    if carta == carta_as:
        carta = carta + 10


    return carta


def jugar_mano_jug():

    #Cartas Jugador
    carta_jug_1 = pedir_carta()
    carta_jug_2 = pedir_carta()

    suma_cartas_jug = carta_jug_1 + carta_jug_2

    if suma_cartas_jug == 21:
        salio_bjn = True
    else:
        salio_bjn = False

    return suma_cartas_jug, carta_jug_1, carta_jug_2, salio_bjn


def jugar_mano_crup():
    #Cartas Crupier
    carta_crup_1 = pedir_carta()

    return carta_crup_1


def pedir_mas_carta_jug(suma_cartas_jug):
    op = int(input('Quiere otra carta? Presione 1 para pedir otra carta, cualquier otro valor para continuar.'))
    while op == 1:
        carta_jug = 0
        if op == 1:
            carta_jug = pedir_carta()

        suma_cartas_jug += carta_jug

        if suma_cartas_jug > 21:
            total_judador = suma_cartas_jug
            return total_judador
        print()
        print("El valor de la carta es: ", carta_jug)
        print('Suma un total de: ', suma_cartas_jug)
        op = int(input('Quiere otra carta? Presione 1 para pedir otra carta, cualquier otro valor para continuar.'))

    else:
        total_jugador = suma_cartas_jug
    return total_jugador


def dar_segunda_car_crup(carta_crup_1):

    carta_crup_2 = pedir_carta()

    suma_cartas_crup = carta_crup_1 + carta_crup_2
    if suma_cartas_crup == 21:
        salio_bjn_crup = True
    else:
        salio_bjn_crup = False
    print('El valor de la 2da Carta del Crupier es: ', carta_crup_2)
    print('El total del Crupier es: ', suma_cartas_crup)
    while suma_cartas_crup <=16:
        carta_crup = pedir_carta()
        print('El valor de la carta del crupier es: ', carta_crup)
        suma_cartas_crup += carta_crup

    total_crupier = suma_cartas_crup

    return total_crupier, carta_crup_2, salio_bjn_crup


def definir_ganador(total_jugador, total_crupier, monto_apostar):
    ganador = ''
    if total_jugador == total_crupier and total_jugador <= 21 and total_crupier <= 21:
        monto_apostar = monto_apostar
        ganador = 'Empate'
    elif total_jugador > 21 and total_crupier > 21:
        ganador = 'Crupier'
        monto_apostar = 0
    elif total_jugador > 21:
        ganador = 'Crupier'
        monto_apostar = 0
    elif total_crupier > 21:
        ganador = 'Jugador'
        monto_apostar = monto_apostar * 2
    elif total_jugador > total_crupier:
        ganador = 'Jugador'
        monto_apostar = monto_apostar * 2
    elif total_crupier > total_jugador:
        ganador = 'Crupier'
        monto_apostar = 0

    return ganador, monto_apostar


def sumar_pozo(pozo):
    print()
    print('Cuanto quiere sumar al pozo ? ')
    suma = int(input('Ingrese el monto de su suma: '))
    while suma <= 0 or (suma + pozo) > 100000:
        print('valor no valido... pruebe con un monto positivo.')
        suma = int(input('Nuevo Monto: '))

    pozo = pozo + suma
    return pozo, suma


def apostar(pozo, puede_jugar):
    monto_apostar = int(input('Ingrese el Monto a Apostar: '))
    #Validar apuesta
    if monto_apostar > pozo:
        print('Su apuesta excele el valor que tiene en su pozo. Ingrese mas dinero en su pozo o apueste un valor menor.')
        monto_apostar = 0
        puede_jugar = False
        return pozo, monto_apostar, puede_jugar
    if monto_apostar % 5 == 0 and monto_apostar <= pozo:
        pozo = pozo - monto_apostar
        puede_jugar = True
        return pozo, monto_apostar, puede_jugar


def validar_pozo():
    #Validar pozo inicial
    pozo = int(input('Ingrese el monto para tener en su pozo: '))
    while pozo < 0 or pozo > 100000:
        print('El pozo no puede superar los 100000 ni tampoco ser negativo... Vuelva a ingresar otro monto.')
        pozo = int(input('Nuevo monto: '))

    return pozo


def porc_victorias_jugador(total_manos, cont_vict_jug):

    if total_manos == 0:
        porcentaje = 0
    else:
        porcentaje = (cont_vict_jug * 100) / total_manos

    return porcentaje


def monto_promedio(acum_pozos, total_manos, pozo):
    if total_manos == 0:
        promedio = pozo
    else:
        promedio = acum_pozos / total_manos
    return promedio


def final():
    #Resultados Finales
    print('******  Resultados  ******')
    print()
    print('Pozo Actualizado: ', pozo)
    print()
    print('El porcentaje de victorias del jugador: ', porc_victorias_jugador(total_manos, cont_vict_jug))
    print('La racha más larga de victorias del croupier: ', max_racha_crup)
    print('La cantidad de manos donde hubo un blackjack natural: ', cont_bj_natural)
    print('El monto máximo que llegó a tener el jugador en el pozo: ', monto_max_pozo)
    print('El monto promedio del que dispuso el jugador para realizar apuestas: ', monto_promedio(acum_pozos, total_manos, pozo))
    print('La pérdida más grande que sufrió el jugador (si hubo alguna)): ', perdida_max)



#Procesos
nombre_jug = input('Ingrese su nombre: ')
pozo = validar_pozo()

opcion = None

while opcion != 3:
    #Menu de Opciones
    print()
    print('Menu de Opciones: ')
    print('1) Apostar.')
    print('2) Jugar una Mano.')
    print('3) Salir.')
    print()

    #Segunda lectura
    opcion = int(input('Ingrese la opcion que Desee: '))

    if opcion == 1:
        pozo, suma = sumar_pozo(pozo)
        print('El monto sumado al pozo fue realizado con exito.')
        print()

    elif opcion == 2:

        acum_pozos += pozo
        print('Opcion 2: Jugar una mano:')
        pozo, monto_apostar, puede_jugar = apostar(pozo, puede_jugar)

        if puede_jugar:
            print()
            print('Pozo: ', pozo, 'Monto a apostar: ', monto_apostar)
            print()
            perd_jug = monto_apostar
            suma_cartas_jug, carta_jug1, carta_jug2, salio_bjn = jugar_mano_jug()
            carta_crup1 = jugar_mano_crup()
            print()
            print('El valor de la 1era carta es: ', carta_jug1, '\n' 'El valor de la 2da carta es: ', carta_jug2)
            print('El valor de la suma de las dos cartas del jugador es de: ', suma_cartas_jug)
            print()
            print('El valor de la 1era carta del Crupier es: ', carta_crup1)
            print()
            total_jugador = pedir_mas_carta_jug(suma_cartas_jug)
            print()
            print('El total del jugador es: ', total_jugador)
            total_crupier, carta_crup2, salio_bjn_crup = dar_segunda_car_crup(carta_crup1)
            print()
            print('El total del Crupier es: ', total_crupier)
            print()
            ganador, monto_apostar = definir_ganador(total_jugador, total_crupier, monto_apostar)
            pozo += monto_apostar
            print('El ganador de esta mano es: ', ganador)
            print('Pozo Actualizado: ', pozo)

            #Racha de victorias mas largas del Crupier
            if ganador == 'Crupier':
                racha_vict_crup += 1
                total_manos += 1
                vict_ant_crup = True
            elif ganador == 'Jugador':
                racha_vict_crup = 0
                vict_ant_crup = False
                cont_vict_jug += 1
                total_manos += 1
            else:
                racha_vict_crup = 0
                vict_ant_crup = False
                total_manos += 1
            #Racha mas alta de victorias del Crupier
            if total_manos == 0:
                max_racha_crup = racha_vict_crup
            elif racha_vict_crup > max_racha_crup:
                max_racha_crup = racha_vict_crup
            # monto maximo en el pozo del jugador
            if total_manos == 0:
                monto_max_pozo = pozo
            elif pozo > monto_max_pozo:
                monto_max_pozo = pozo

            #Perdida maxima del jugador
            if total_manos == 0:
                perdida_max = 0
            elif ganador == 'Crupier':
                if perd_jug > perdida_max:
                    perdida_max = perd_jug
            #contar BJ Natural
            if salio_bjn or salio_bjn_crup:
                cont_bj_natural += 1

final()


