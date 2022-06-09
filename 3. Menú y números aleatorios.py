import random

menu = 'Menu de Opciones \n' \
        '=========================================================' + '\n' \
        'Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]. \n' \
        'Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].   \n' \
        'Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] \
         y calcular el valor promedio de los números menores a 10.000.\n' \
        'Cualquier otro numero -- Salir  \n'

acumulador = 0


#Ciclo

print(menu)

opcion = int(input('Ingrese la opcion que desee: ')) 

while opcion > 0 and opcion <= 3:
    #Procesos
    if opcion == 1:
        print('Opcion 1')
        f = 0
        while f < 1000:
            n = random.randint(0, 100000)
            acumulador += n
            f += 1
        prom1 = acumulador / 1000
        print('El promedio es: ', prom1)

    elif opcion == 2:
        print('Opcion 2')
        may = i = 0 
        while i < 10000:
            n = random.randint(0, 100000)
            if may < n:
                may = n
            i += 1
        print('El mayor es: ', may) 
    else:
        print('Opcion 3')
        men = 0
        x = 0
        while x < 5000:
            n = random.randint(0, 100000)
            if men > n:
                men = n 
            x += 1
        print('El menor es: ', men)
    print()
    print(menu)
    #Segunda lectura
    opcion = int(input('Ingrese la opcion que desee: '))    
else:
    print('Programa terminado.')

