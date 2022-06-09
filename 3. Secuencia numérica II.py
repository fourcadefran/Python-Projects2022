# Datos
n = int(input('Ingrese el valor del numero: '))
anterior = 0
ct = 0
cont6 = acu6 = 0
cont_div_ant = 0

#Procesos


while n != 0:
    ct += 1

    if n % 6 == 0:
        cont6 += 1
        acu6 += n

    if ct == 0:
        pass
    else:
        if n % anterior == 0:
            cont_div_ant += 1


    anterior = n
    n = int(input('Ingrese el siguiente valor del numero: '))

if cont6 > 0:
    promedio = acu6 / cont6

else:
    promedio = 0

#Resultados

print()
print('El promedio de los multiplos por 6 es: ', promedio)
print()
print('Cantidad de numeros que son exactamente divisibles por su anterior: ', cont_div_ant)
print()
print()
