# datos

acumulador_acotado = 0
contador_pares = 0
contador_impares = 0
aparecio0 = False

#procesos

i = int(input('Ingrese un numero: (con negativo corta)'))

while i >= 0:


    if 50 <= i <= 100:
        acumulador_acotado += i

    if i % 2 > 0:
        contador_impares += 1
    else:
        contador_pares +=1

    if i == 0:
        aparecio0 = True

    i = int(input('Ingrese un numero: (con negativo corta)'))

else:
    print('Programa terminado')
print()
#Resultados
print('sumatoria de numeros entre 50 y 100: ', acumulador_acotado)
print()
print('Contador de pares: ', contador_pares)
print()
print('Contador de impares: ', contador_impares)
print()
if aparecio0:
    print('aparecio un cero')
else:
    print('No aparecio un cero')
print()
if contador_impares == 0:
    print('Serie solo de pares')
else:
    print('Serie solo de impares')
