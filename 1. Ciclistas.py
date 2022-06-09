# Datos
n = int(input('Ingrese por teclado la cantidad de competidores: '))

record = int(input('Ingrese el tiempo record del circuito: '))
primer_competidor = True
acumulador_tiempo = 0
# Procesos

for i in range(n):
    #procesos
    nombre = input('Ingrese el nombre del competidor: ')

    tiempo = int(input('Ingrese el tiempo del competidor: '))

    # a)
    if primer_competidor == True:
        ganador_tiempo = tiempo
        ganador_nombre = nombre
        primer_competidor = False

    elif tiempo < ganador_tiempo:
        ganador_nombre = nombre
        ganador_tiempo = tiempo

    #c)
    acumulador_tiempo += tiempo

if n > 0:
    prom = acumulador_tiempo / n
else:
    prom = 0

#Resultados
print()
print('El ganador es: ', ganador_nombre, ' Con un tiempo: ', ganador_tiempo)
print()

#b)
if ganador_tiempo < record:
    print('Se supero el record del circuito. ')
else:
    print('No se supero el record.')
print()
print('El promedio de tiempo es: ', prom)
