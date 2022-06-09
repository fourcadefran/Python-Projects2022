# Datos
import random

n = 1000
random.seed(52)
inicio = 1
fin = 2500

div4 = 0
div_ambos = 0
prom = cont2mil = acum2mil = 0
menor = 0
porcentaje = 0
aparecio = False

# procesos

for i in range(n):
    num = random.randint(inicio, fin)

    if num % 4 == 0:
        if num % 8 == 0:
            div_ambos += 1
        else:
            div4 += 1

    if num > 2000:
        cont2mil += 1
        acum2mil += num

    if i == 0:
        primer_numero = num
    elif num < primer_numero:
        menor += 1

    if num == 1 or num == 2500:
        aparecio = True

if cont2mil > 0:
    prom = acum2mil / cont2mil
else:
    prom = 0

porcentaje = (menor * 100) / n

# Resultados

print()
print('los numeros divisibles por 4 pero no por 8 son: ', div4, 'Los numeros divisibles por ambos son: ', div_ambos)
print()
print('El promedio de los mayores a 2000: ', prom)
print()
print('Cuantos numeros eran menor al primer valor: ', menor, 'porcentaje que representa del total: ', porcentaje)
print()
if aparecio:
    print('aparecieron los extremos.')
else:
    print('No apareceieron los extremos')
