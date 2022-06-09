# Datos
izq = int(input('Cargue el 1er numero: '))

der = int(input('Cargue el 2do numero: '))

# Procesos
print()
print('Impares de forma ascendente: ')
for i in range(izq, der + 1):
    if i % 2 > 0:
        print(i)

print()
print('Impares de forma descendente: ')
for i in range(der, izq - 1, -1):
    if i % 2 > 0:
        print(i)

