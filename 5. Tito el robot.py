#Datos
import random

posicionx = random.randint(-50, 50)
posiciony = random.randint(-50, 50)
pasos = 0
#Procesos

#Validar bateria
bateria = int(input('Ingresar la cantidad de bateria del robot: '))
while bateria < 35 or bateria > 100:
    print('Valor incorrecto, ingrese un valor entre 35 y 100.')
    bateria = int(input('Ingrese un valor valido: '))


opcion = None
while opcion != 'x' and opcion != 'X':
    print()
    print('*' * 50)
    print()
    print('Posicion del robot: Y = ', posiciony, '  X = ', posicionx)
    print()
    print('Menu de opciones: ')
    print('Opcion a): ...')
    print('Opcion b): ...')
    print('Opcion c): ...')
    print('Opcion d): ...')
    print('Opcion e): ...')
    print('*' * 50)
    print()
    #2da lectura
    opcion = input('Elija una opcion: ')

    if opcion == 'a':
        print('Opcion a)')
        posiciony += 10
        pasos += 10
        bateria -= 10

    elif opcion == 'b':
        print('Opcion b)')
        posiciony -= 20
        pasos += 20
        bateria -= 20
    elif opcion == 'c':
        print('Opcion c)')
        posicionx += 10
        pasos += 10
        bateria -= 10
    elif opcion == 'd':
        print('Opcion d)')
        posicionx -= 20
        pasos += 20
        bateria -= 10
    elif opcion == 'e':
        print('Opcion e)')
        print('Bateria: ', bateria)
        print('Pasos: ', pasos)
    else:
        print('Valor invalido. Ingrese otro.')

print('Programa terminado')
