#Datos

n = int(input('Ingrese la cantidad de numeros a procesar: '))

menor = seg_menor =  0
primera_vuelta = True
prom = cont_pos = acu_pos = 0

mayor = 0
primer_neg = True
# Procesos

for i in range(n):
    #procesos
    numero = int(input('Ingrese el numero a procesar: '))

    if primera_vuelta:
        menor = seg_menor = numero
        primera_vuelta = False
    elif menor > numero:
        seg_menor = menor
        menor = numero

    if numero > 0:
        acu_pos += numero
        cont_pos += 1

    elif numero < 0:
        if primer_neg:
            mayor = numero
            primer_neg = False
        elif numero < mayor:
            mayor = numero

if cont_pos > 0:
    prom = acu_pos / cont_pos
else:
    prom = 0

#Resultados
print(menor)
print('El segundo menor es: ', seg_menor)
print()
print('El promedio de los positivos es: ', prom)
print()
print('El mayor de los negativos: ', mayor)

