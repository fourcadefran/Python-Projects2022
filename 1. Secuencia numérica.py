#Datos
n = int(input('Ingrese el numero a procesar: '))

cd3 = ct = 0
anterior = 0
ccuadrados = 0
may = pos = 0
primero = True
# Procesos

while n != 0:
    ct += 1
    if n % 3 == 0:
        cd3 += 1
    if n == anterior ** 2:
        ccuadrados += 1

    if n % 2 != 0:
        if primero:
            may = n
            pos = 1
            primero = False
        else:
            if n > may:
                may = n
                pos = ct

    anterior = n
    n = int(input('Ingrese el siguiente numero: '))

if cd3 > 0:
    porcentaje = (cd3 * 100) / ct
else:
    porcentaje = 0

#Resultados
print()
print('El porcentaje es: ', porcentaje)
print()
print('cantidad de numeros que son el cuadrado del anterior: ', ccuadrados)
print()
print('La posicion del mayor de los numeros impares: ', pos)
print(ct)
