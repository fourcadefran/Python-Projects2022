# datos
acumulador_sueldos = 0
menor_sueldo = 0
mayor_sueldo = 0
aguinaldo = 0
primer_sueldo = True
mes_menor_sueldo = 0

#procesos

for i in range(6):
    print('Mes numero: ', i + 1)
    sueldo = int(input('Ingrese el sueldo del mes: '))

    if primer_sueldo:
        menor_sueldo = sueldo
        mes_menor_sueldo = i + 1
        primer_sueldo = False

    elif menor_sueldo > sueldo:
        mayor_sueldo = menor_sueldo
        menor_sueldo = sueldo
        mes_menor_sueldo = i


    acumulador_sueldos += sueldo

aguinaldo = mayor_sueldo / 2

prom = acumulador_sueldos / 6
#Resultados

print()
print('El aguinaldo es: ', aguinaldo)
print()
print('El menor sueldo es: ', menor_sueldo, 'En el mes: ', mes_menor_sueldo)
print()
print('El promedio de sueldo es de: ', prom)
