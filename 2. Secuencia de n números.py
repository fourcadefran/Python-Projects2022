#Datos

n = int(input('Ingrese un numero mayor a cero(0): '))
contador5 = 0
anterior = 0
cont_mayor_ant = 0
ct = 0
primer_numero = cont_primer = 0

while n > 0:

    ct += 1
    if ct == 1:
        primer_numero = n
    else:
        if n == primer_numero:
            cont_primer += 1
        if n > anterior:
            cont_mayor_ant += 1

    car = str(n)
    if car[-1] == '5':
        contador5 += 1

    anterior = n
    n = int(input('Ingrese un nuevo valor mayor a cero(0): '))

#Resultados
print()
print('La cantidad de 5 es igual a: ', contador5)
print()
print('la cantidad de numeros que son mayores a su anterior: ', cont_mayor_ant)
print()
print('Aparece: ', cont_primer, ' veces el primer numero en la secuencia')

