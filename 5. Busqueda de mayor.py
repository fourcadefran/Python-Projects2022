import random

#Datos
may = i = 0

#Procesos

while i < 10000:
    n = random.randint(0, 100000)
    if may < n:
        may = n
    i += 1

print('El mayor es: ', may)
