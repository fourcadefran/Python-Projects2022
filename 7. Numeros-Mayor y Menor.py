# Datos 
n = int(input('Ingrese la cantidad de numeros a procesar: '))
may_par = 0 
men_impar = 0
 

#Procesos

for i in range(n):
    # procesos
    numero = int(input('Ingrese el numero a procesar: '))
    if i == 0:
        if numero % 2 == 0: 
            may_par = numero
    elif numero % 2 == 0 and numero > may_par:
        may_par = numero 
    
    if i == 0:
        if numero % 2 != 0:
            men_impar = numero 
    elif numero % 2 > 0 and numero < men_impar:             #Revisar asignacion del menor !!!!!
        men_impar = numero 

# Resultados 

print()
print('El mayor de los pares es: ', may_par)
print()
print('El menor de los impares es: ', men_impar)

#Plantear con un while

n = int(input('Ingrese el numero a procesar (con cero termina): '))
primer_impar = True 
menor_impar = mayor_par = 0


while n != 0:
    paridad = n % 2
    if paridad == 0:
        if n > mayor_par:
            mayor_par = n 
    else:
        if primer_impar or n < menor_impar:
            primer_impar = False
            menor_impar = n 

    n = int(input('Cargue el siguente numero: '))

if mayor_par != 0:
    print('El mayor numero de los pares es:', mayor_par)
else:
    print('No ingreso numeros pares')

if menor_impar != 0:
    print('El menor numero de los impares es:', menor_impar)
else:
    print('No ingreso numeros impares')
