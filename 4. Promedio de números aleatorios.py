import random
# Datos
acumulador = 0
#Procesos

f = 0
while f < 1000:
    n = random.randint(0, 100000)
    acumulador += n
    f += 1

prom1 = acumulador / 1000
print('El promedio es: ', prom1)
