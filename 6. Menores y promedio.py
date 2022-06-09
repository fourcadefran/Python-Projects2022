# datos
import random

acumulador_menores = contador_menores = men = 0

# procesos
i = 0
while i < 5001:
    n = random.randint(1, 100000)
    if men > n:
        men = n
    if n < 10000:
        acumulador_menores += n
        contador_menores += 1
    i += 1

prom = acumulador_menores / contador_menores
#Resultados
print("El menor es: ", men)
print('Promedio de los menores a 10000: ', prom)

